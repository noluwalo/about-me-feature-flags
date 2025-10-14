# LaunchDarkly & Segment Analytics Demo - About Me Page

A Flask-based "About Me" demo application showcasing **LaunchDarkly feature flags** and **Segment Analytics integration**, with personalized experiences for different user roles (Recruiter vs Teammate).

## 🎯 Features

- **LaunchDarkly Feature Flags**:
  - `type-writer-animation`: Toggle typewriter animation effect
  - `mode-toggle`: Switch between Professional (Recruiter) and Fun (Teammate) modes
  - `dynamic-content-widget`: Dynamic content variations
  - `show-debug-panel`: Show/hide debug panel

- **Segment Analytics Integration**:
  - Real-time event tracking
  - User identification
  - Custom event properties

- **Role-Based Experiences**:
  - Professional mode for Recruiters with career highlights
  - Fun mode for Teammates with personal interests

## 📋 Prerequisites

- Python 3.8 or higher
- A LaunchDarkly account (free tier available at [launchdarkly.com](https://launchdarkly.com))
- A Segment account (free tier available at [segment.com](https://segment.com))

## 🚀 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git
cd YOUR-REPO-NAME
```

### 2. Install Dependencies

```bash
pip install flask flask-cors gunicorn launchdarkly-server-sdk
```

### 3. Set Up LaunchDarkly

#### a) Get Your SDK Key
1. Log in to your [LaunchDarkly account](https://app.launchdarkly.com)
2. Go to **Account settings** → **Projects** → Your project
3. Copy your **SDK key** (starts with `sdk-`)

#### b) Create Feature Flags
Create the following feature flags in your LaunchDarkly project:

| Flag Key | Type | Variations | Default Value |
|----------|------|------------|---------------|
| `type-writer-animation` | Boolean | true/false | false |
| `mode-toggle` | String | "professional", "fun" | "professional" |
| `dynamic-content-widget` | String | "books", "other" | "books" |
| `show-debug-panel` | Boolean | true/false | false |

#### c) Configure Flag Targeting (Optional)
- For `mode-toggle`: Create a rule where `role = "recruiter"` serves `"professional"`, and `role = "teammate"` serves `"fun"`
- Turn ON all flags for testing

#### d) Update SDK Key in Code
In `app.py` (line 22), replace the SDK key with yours:
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

Or create a `.env` file:
```
SEGMENT_WRITE_KEY=your-segment-write-key-here
```

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
   - Name
   - Email
   - Select role: **Recruiter** (Professional mode) or **Teammate** (Fun mode)
3. **Click Submit** to see personalized content based on LaunchDarkly flags
4. **Toggle modes** using the toggle button to see different experiences
5. **Click "Surprise Me!"** to see dynamic content variations

## 🔍 What to Test

### Feature Flag Testing
- **Typewriter Animation**: Toggle this flag ON/OFF in LaunchDarkly to see animated text
- **Mode Toggle**: Change targeting rules to serve different modes to different roles
- **Debug Panel**: Turn this flag ON to see real-time flag values (appears at bottom of page)

### Segment Analytics Testing
1. Go to your Segment **Debugger** page
2. Submit the form and interact with the app
3. You should see events like:
   - `User Submitted Form`
   - `Mode Toggle Clicked`
   - `Surprise Clicked`

## 📁 Project Structure

```
├── app.py                    # Flask backend with LaunchDarkly integration
├── templates/
│   └── index.html           # Frontend with Segment Analytics
├── static/
│   └── images/              # Personal photos
├── requirements.txt         # Python dependencies (if using pip)
└── README.md               # This file
```

## 🔑 Important Notes

### Security
- **Never commit API keys** to the repository
- Use environment variables for secrets
- The SDK key in `app.py` should be replaced with your own
- For production, use proper secret management

### LaunchDarkly Context
The app sends user context to LaunchDarkly with these attributes:
- `email`: User's email address
- `name`: User's name
- `role`: "recruiter" or "teammate"
- `location`: User's location
- `interest`: User's interest

You can create custom targeting rules based on these attributes.

## 🛠 Troubleshooting

### LaunchDarkly Connection Issues
- Check that your SDK key is correct
- Verify the SDK initialized successfully (check console logs: `✅ SDK successfully initialized`)
- Ensure feature flags exist in LaunchDarkly with exact key names

### Segment Not Tracking
- Verify your `SEGMENT_WRITE_KEY` environment variable is set
- Check browser console for Segment initialization messages
- Go to Segment Debugger to see real-time events

### Flags Not Updating
- Refresh the page after changing flags in LaunchDarkly
- Check LaunchDarkly Live Events to see flag evaluations
- Verify targeting rules aren't blocking the flag

## 📊 Demo Credentials (For Testing)

You can test with these sample users:
- **Recruiter**: `recruiter@example.com`, Role: Recruiter
- **Teammate**: `teammate@example.com`, Role: Teammate

## 📝 License

This is a demo project for educational purposes.

## 🙋 Questions?

If you run into issues, check:
1. Python version is 3.8+
2. All dependencies are installed
3. LaunchDarkly flags are created with correct keys
4. Environment variables are set correctly
5. Port 5000 is not in use by another application
