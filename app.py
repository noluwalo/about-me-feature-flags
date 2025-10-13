#"""
#Flask Backend with LaunchDarkly Integration
#"""

from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
import ldclient
from ldclient.config import Config
from ldclient import Context
import os

# ============================================
# INITIALIZE FLASK APP
# ============================================
app = Flask(__name__)
CORS(app)

# ============================================
# INITIALIZE LAUNCHDARKLY CLIENT
# ============================================
# Set your LaunchDarkly SDK key
LAUNCHDARKLY_SDK_KEY = os.environ.get('LAUNCHDARKLY_SDK_KEY', 'sdk-c33b0d5d-5bb8-4b17-8b92-7191ab9abf7a')

ldclient.set_config(Config(LAUNCHDARKLY_SDK_KEY))
ld_client = ldclient.get()

# Check if SDK initialized successfully
if not ld_client.is_initialized():
    print('❌ SDK failed to initialize')
else:
    print('✅ SDK successfully initialized')
    
    # Tracking your memberId lets LaunchDarkly know you are connected
    tracking_context = (
        Context.builder('user-key-123abcde')
        .kind('user')
        .set('email', 'biz@face.dev')
        .build()
    )
    ld_client.track('68e01bdc6818ca09d507d02d', tracking_context)
    print('📊 Tracking event sent to LaunchDarkly')

# ============================================
# ROUTE 1: SERVE THE HOMEPAGE
# ============================================
@app.route('/')
def index():
    return render_template('index.html')

# ============================================
# ROUTE 2: GET FEATURE FLAGS FOR A USER
# ============================================
@app.route('/api/feature-flags', methods=['POST'])
def get_feature_flags():
    user_data = request.json

    print(f"\n📥 Received request for user: {user_data.get('email', 'unknown')}")
    print(f"   Role: {user_data.get('role', 'unknown')}")

    # Build LaunchDarkly Context
    context = Context.builder(user_data['email']) \
        .kind('user') \
        .name(user_data.get('name', 'Anonymous')) \
        .set('role', user_data.get('role', 'general')) \
        .set('location', user_data.get('location', 'Unknown')) \
        .set('interest', user_data.get('interest', 'general')) \
        .build()

    print(f"   ✅ Built LaunchDarkly context")

    # Evaluate feature flags
    typewriter_animation = ld_client.variation(
        'typewriter-animation',
        context,
        False  # Default: OFF
    )
    print(f"   🚩 typewriter-animation: {typewriter_animation}")

    mode_toggle = ld_client.variation(
        'mode-toggle',
        context,
        'professional'  # Default: professional
    )
    print(f"   🚩 mode-toggle: {mode_toggle}")

    surprise_variant = ld_client.variation(
        'dynamic-content-widget',
        context,
        'books'  # Default: books
    )
    print(f"   🚩 dynamic-content-widget: {surprise_variant}")

    show_debug_panel = ld_client.variation(
        'show-debug-panel',
        context,
        False  # Default: hidden
    )
    print(f"   🚩 show-debug-panel: {show_debug_panel}")

    # Return flags to frontend
    flags = {
        'typewriter_animation': typewriter_animation,
        'mode_toggle': mode_toggle,
        'surprise_variant': surprise_variant,
        'show_debug_panel': show_debug_panel
    }

    print(f"   📤 Sending flags back to frontend\n")
    return jsonify(flags)

# ============================================
# ROUTE 3: HEALTH CHECK
# ============================================
@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({
        'status': 'healthy',
        'launchdarkly': 'connected',
        'message': 'Flask backend is running!'
    })

# ============================================
# ROUTE 4: GET SEGMENT WRITE KEY
# ============================================
@app.route('/api/segment-key', methods=['GET'])
def get_segment_key():
    segment_key = os.environ.get('SEGMENT_WRITE_KEY', '')
    return jsonify({'writeKey': segment_key})

# ============================================
# CLEANUP
# ============================================
# Note: In production with gunicorn, we let the LaunchDarkly client 
# stay open for the lifetime of the worker process. It will be cleaned 
# up automatically when the worker shuts down.
import atexit

@atexit.register
def close_ld_client():
    ld_client.close()
    print("👋 LaunchDarkly client closed")

# ============================================
# START THE FLASK SERVER
# ============================================
if __name__ == '__main__':
    print("\n" + "="*50)
    print("🚀 Starting Flask Server with LaunchDarkly")
    print("="*50)
    print("📍 Server running at: http://localhost:5000")
    print("📍 API endpoint: http://localhost:5000/api/feature-flags")
    print("📍 Health check: http://localhost:5000/api/health")
    print("="*50 + "\n")

    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )