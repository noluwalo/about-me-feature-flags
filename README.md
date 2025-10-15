# LaunchDarkly & Segment Analytics Demo - About Me Page

A Flask-based "About Me" demo application showcasing **LaunchDarkly feature flags** and **Segment Analytics integration**, with personalized experiences for different user roles (Recruiter vs Teammate).

## 🎯 Features

- **LaunchDarkly Feature Flags**:
  - `type-writer-animation`: Boolean flag to toggle typewriter animation effect
  - `mode-toggle`: Multi-variate flag to switch between Professional (Recruiter) and Fun (Teammate) modes
  - `dynamic-content-widget`: A/B test for "Surprise Me!" button - serves either book recommendations or fun facts
  - `show-debug-panel`: Demo-only debug panel (not a production flag, just for visualization)

- **Segment Analytics Integration & Metrics**:
  - Real-time event tracking for all user interactions
  - User identification with auto-generated profiles
  - Custom event properties for detailed analytics
  - **Why Segment?** Acts as a data hub that captures events and forwards them to LaunchDarkly for experiment metrics, plus other destinations (Google Analytics, etc.)
  - Use Segment-tracked events to create metrics and run experiments in LaunchDarkly

- **Role-Based Experiences**:
  - Professional mode for Recruiters with career highlights
  - Fun mode for Teammates with personal interests

## 📋 Prerequisites

- Python 3.8 or higher
- A LaunchDarkly account (free tier available at [launchdarkly.com](https://launchdarkly.com))
- A Segment account (free tier available at [segment.com](https://segment.com))

## 🔍 LaunchDarkly Observability Plugin

This project includes the **LaunchDarkly Observability Plugin** (added for exploration and learning):
- **Service telemetry**: Tracks SDK operations with OpenTelemetry
- **Custom logging**: Records important events and user interactions
- **Span tracking**: Monitors feature flag evaluation performance
- **Real-time insights**: View traces and logs in LaunchDarkly dashboard

*Note: This was implemented to explore advanced SDK features and is not required for basic flag functionality.*

## 🚀 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git
cd YOUR-REPO-NAME
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

Or install individually:
```bash
pip install flask flask-cors gunicorn launchdarkly-server-sdk launchdarkly-observability
```

### 3. Set Up LaunchDarkly

#### a) Get Your SDK Key
1. Log in to your [LaunchDarkly account](https://app.launchdarkly.com)
2. Go to **Account settings** → **Projects** → Your project
3. Copy your **SDK key** (starts with `sdk-`)

#### b) Create Feature Flags
Create the following feature flags in your LaunchDarkly project:

| Flag Key | Type | Variations | Default Value | Purpose |
|----------|------|------------|---------------|---------|
| `type-writer-animation` | Boolean | true/false | false | Part 1: Toggle UI feature |
| `mode-toggle` | String | "professional", "fun" | "professional" | Part 2: User targeting by role |
| `dynamic-content-widget` | String | "books", "fun-facts" | "books" | Part 3: A/B test for Surprise button |
| `show-debug-panel` | Boolean | true/false | false | Demo visualization only |

#### c) Configure Flag Targeting
- **For `mode-toggle`**: Create a rule where `role = "recruiter"` serves `"professional"`, and `role = "teammate"` serves `"fun"`
- **For `dynamic-content-widget`**: Set up A/B test with 50/50 split between "books" and "fun-facts" variations
- Turn ON all flags for testing

#### d) Update SDK Key in Code
In **`app.py` (line 27)**, replace the SDK key with yours:
```python
LAUNCHDARKLY_SDK_KEY = os.environ.get('LAUNCHDARKLY_SDK_KEY', 'YOUR-SDK-KEY-HERE')
```

### 4. Set Up Segment Analytics

#### a) Get Your Write Key
1. Log in to your [Segment account](https://app.segment.com)
2. Go to **Connections** → **Sources**
3. Create a new **JavaScript** source (or use existing)
4. Copy your **Write Key**

#### b) Set Environment Variable
```bash
export SEGMENT_WRITE_KEY='your-segment-write-key-here'
```

Or in **`app.py` (line 127)**, you can hardcode it temporarily for testing:
```python
segment_key = os.environ.get('SEGMENT_WRITE_KEY', 'YOUR-WRITE-KEY-HERE')
```

#### c) Connect Segment to LaunchDarkly (Extra Credit)
1. In Segment, go to **Connections** → **Destinations**
2. Add **LaunchDarkly** as a destination
3. Configure it to send events to LaunchDarkly for experiment metrics
4. Now your tracked events can power LaunchDarkly experiments!

### 5. Run the Application

```bash
# Option 1: Using Flask directly (development)
python app.py

# Option 2: Using Gunicorn (production-like)
gunicorn --bind=0.0.0.0:5000 --reuse-port app:app
```

The app will be available at: **http://localhost:5000**

## 🎮 How to Use

1. **Open the app** in your browser at `http://localhost:5000`
2. **Enter your details**:
   - Name (email is auto-generated from name for user tracking)
   - Select role: **Recruiter** (Professional mode) or **Teammate** (Fun mode)
3. **Click Submit** to see personalized content based on LaunchDarkly flags
4. **Toggle modes** using the toggle button to see different experiences
5. **Click "Surprise Me!"** to see A/B test variations (book recommendations or fun facts)
6. **[Debug Panel]** button shows real-time flag values if `show-debug-panel` flag is ON

## 🔍 What to Test

### Part 1: Boolean Feature Flag
- **Typewriter Animation**: Toggle `type-writer-animation` flag ON/OFF in LaunchDarkly to see animated vs static text

### Part 2: Multi-variate Flag with Targeting
- **Mode Toggle**: The `mode-toggle` flag serves different modes based on user role:
  - Recruiters see "professional" mode with career highlights
  - Teammates see "fun" mode with personal interests

### Part 3: A/B Experiment
- **Dynamic Content Widget**: The `dynamic-content-widget` flag powers an A/B test:
  - Variation "books" → Shows book recommendations when clicking "Surprise Me!"
  - Variation "fun-facts" → Shows fun facts when clicking "Surprise Me!"
- **Hypothesis**: Fun facts increase engagement more than book recommendations
- **Metric**: Track click count via Segment events

### Segment Analytics & Metrics
1. Go to your Segment **Debugger** page
2. Submit the form and interact with the app
3. You should see tracked events:
   - `User Submitted Form`
   - `Mode Toggle Clicked`
   - `Surprise Clicked` (with variant and click count)
4. These events flow to LaunchDarkly for experiment metrics

## 📁 Project Structure

```
├── app.py                    # Flask backend with LaunchDarkly SDK integration
├── templates/
│   └── index.html           # Frontend with Segment Analytics JavaScript
├── static/
│   └── images/              # Personal photos for demo
├── requirements.txt         # Python dependencies
└── README.md               # This file
```

## 🔑 Important Notes

### How User Identification Works
- Users enter their **name only** (no email input)
- The app auto-generates an email as `{name}@example.com` for Segment user profiles
- This allows Segment to track events and attach them to a user identity
- LaunchDarkly receives user context with name, role, and generated email

### LaunchDarkly Context
The app sends user context to LaunchDarkly with these attributes:
- `name`: User's name
- `role`: "recruiter" or "teammate" 
- `location`: User's location
- `interest`: User's interest

You can create custom targeting rules based on these attributes.

### Security
- **Never commit API keys** to the repository
- Use environment variables for secrets
- Replace placeholder SDK keys in:
  - **`app.py` line 27**: LaunchDarkly SDK key
  - **`app.py` line 127**: Segment Write Key (via environment variable)
- For production, use proper secret management

## 🛠 Troubleshooting

### LaunchDarkly Connection Issues
- Check that your SDK key is correct in `app.py` line 27
- Verify the SDK initialized successfully (check console logs: `✅ SDK successfully initialized`)
- Ensure feature flags exist in LaunchDarkly with exact key names (case-sensitive)

### Segment Not Tracking
- Verify your `SEGMENT_WRITE_KEY` environment variable is set
- Check browser console for Segment initialization messages: `✅ Segment Analytics initialized`
- Go to Segment Debugger to see real-time events
- Make sure events show the correct properties (variant, clicks, role, etc.)

### Flags Not Updating
- Refresh the page after changing flags in LaunchDarkly
- Check LaunchDarkly Live Events to see flag evaluations in real-time
- Verify targeting rules aren't blocking the flag (check user context attributes)

### A/B Test Not Working
- Ensure `dynamic-content-widget` flag has variations "books" and "fun-facts"
- Check that targeting/rollout is set up correctly (try 50/50 split)
- Verify Segment events are tracking the correct variant

## 📝 License

This is a demo project for educational purposes.

## 🙋 Questions?

If you run into issues, check:
1. Python version is 3.8+
2. All dependencies are installed (`pip install -r requirements.txt`)
3. LaunchDarkly flags are created with correct keys
4. Environment variables are set correctly (`SEGMENT_WRITE_KEY`)
5. Port 5000 is not in use by another application
6. SDK keys are updated in `app.py` (lines 27 and 127)

---

## 🎉 Assessment Summary

This project demonstrates:

✅ **Part 1**: Boolean feature flag for UI features (`type-writer-animation`)  
✅ **Part 2**: Multi-variate flag with user targeting (`mode-toggle` by role)  
✅ **Part 3**: A/B experiment with hypothesis testing (`dynamic-content-widget`)  
✅ **Metrics**: Event tracking via Segment integration for experiment metrics  
✅ **Documentation**: Clear setup instructions & code comments  
✅ **Runnable**: Works locally and on Replit  
✅ **Extra Credit**: Segment → LaunchDarkly integration for advanced analytics and experimentation
