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

## 🌐 Live Demo

**Try the published website here:** [https://b93cf3d1-66b7-4349-863d-b1c51311cb49-00-2cizuga4iat8t.picard.replit.dev](https://b93cf3d1-66b7-4349-863d-b1c51311cb49-00-2cizuga4iat8t.picard.replit.dev)

This live demo is a **published website** connected to my **LaunchDarkly account** with **all flags turned ON** AND my **full Segment account** for end-to-end tracking:
- ✅ Typewriter animation is active
- ✅ Role-based targeting is configured (Recruiter → Professional, Teammate → Fun)
- ✅ A/B test is running for the "Surprise Me!" button
- ✅ Debug panel is enabled
- ✅ Segment events tracked in real-time

**To see live flags:** Click the **[Debug]** button at the bottom of the page to view real-time flag values and their current state.

**To see Segment tracking:** The app displays visual pop-ups showing all events being tracked and sent to Segment in real-time - including the events used for **metrics configuration in the Extra Credit (Part 3)** section. Perfect for those without a full Segment account to see the end-to-end integration in action!

**See the full demo in action below** ⬇️

## 🎮 Explore the Live Demo (Understand What You're Building)

**Interact with the live site to see all features in action:**

1. **Start Exploring:** Open the published website and enter your name
2. **Choose Your Experience:** Select "Recruiter" or "Teammate" to see role-based targeting
   - On the second screen, notice the **typewriter animation** automatically displaying my name character-by-character
   - This is controlled by the `type-writer-animation` boolean flag (currently ON) - demonstrating **Part 1: Release and remediate with boolean flags**
   - Notice how the same app shows completely different content based on your role (Professional vs Fun mode)
   - This demonstrates **role-based targeting** with multi-variate flags

3. **Watch Real-Time Tracking:** As you interact, visual pop-ups appear showing:
   - Every event being sent to Segment
   - User identification and properties
   - Event data that powers LaunchDarkly experiments
   - This demonstrates the **Segment → LaunchDarkly metrics integration**

4. **See the A/B Test:** Click the "Surprise Me!" button multiple times
   - You'll get either book recommendations OR fun facts (50/50 split)
   - Each click is tracked as a metric event
   - This demonstrates **Part 3: A/B experimentation with metrics**

5. **Toggle Between Modes:** Click the mode toggle button
   - Watch the entire page transform (Professional ↔️ Fun)
   - See how feature flags control UI/UX dynamically
   - This demonstrates **Part 1: Boolean flags for UI features**

6. **View Live Flags:** Click the [Debug] button at the bottom
   - See which flags are ON/OFF in real-time
   - View current values (typewriter animation, mode, variant)
   - Understand how flags control the entire experience

**By exploring the live demo, you'll understand exactly how LaunchDarkly flags + Segment analytics work together to create personalized, measurable user experiences!**

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

**For `type-writer-animation`** (Boolean flag):
1. Turn the flag **ON** (toggle to the right)
2. Under "Default rule", select **"Serve: true"**
3. Save changes
4. All users will now see the animated typewriter effect for the name display

**For `mode-toggle`** (Multi-variate targeting):
1. Turn the flag **ON**
2. Add targeting rule: 
   - **IF** `role` **is one of** `recruiter` → **THEN serve** `professional`
   - **IF** `role` **is one of** `teammate` → **THEN serve** `fun`
3. Default rule: Serve `professional`
4. Save changes

**For `dynamic-content-widget`** (A/B test):
1. Turn the flag **ON**
2. Set up percentage rollout for A/B test:
   - 50% → `books`
   - 50% → `fun-facts`
3. Or create targeting rules by user attributes
4. Save changes
5. **Create metric and experiment** (see detailed instructions in "Step 4: Create Metrics in LaunchDarkly" and "Step 5: Attach Metric to Experiment" sections below)

**For `show-debug-panel`** (Demo only):
1. Turn **ON** to show debug panel
2. Serve `true` to everyone
3. Users will see [Debug] button at bottom of page

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

#### c) Connect Segment to LaunchDarkly for Metrics (Extra Credit)

This integration allows Segment events to power LaunchDarkly experiment metrics.

**Step 1: Get LaunchDarkly Client-side ID**
1. In LaunchDarkly, go to **Account settings** → **Projects** → Your project
2. Select your environment (e.g., Production, Test)
3. Copy the **Client-side ID** (starts with a random string like `63a1e2b3c4d5e6f7`)

**Step 2: Add LaunchDarkly Destination in Segment**
1. In Segment, go to **Connections** → **Catalog**
2. Search for **"LaunchDarkly (Actions)"** and click it
3. Click **Configure LaunchDarkly (Actions)**
4. Select your JavaScript source (the one tracking events)
5. Click **Next** and name it (e.g., "LaunchDarkly Metrics")
6. Paste your **LaunchDarkly Client-side ID** from Step 1
7. Click **Create Destination**

**Step 3: Map Track Events to Metrics**
1. In the LaunchDarkly destination settings, click **Mappings** tab
2. Click **New Mapping** → Select **Track Event** action
3. Configure the field mappings as follows:

| Segment Field | LaunchDarkly Field | Mapping | Example Value |
|---------------|-------------------|---------|---------------|
| `event` | Event Name | `{{ event }}` | "Surprise Clicked" |
| `userId` | Email | `{{ userId }}` | "agvbsdbrtf@example.com" |
| `anonymousId` | Context Key | `{{ anonymousId }}` | "7c42798e-10c1-4a70-838a-58a8cdbf5754" |
| (fixed value) | Context Kind | `user` | "user" |
| `properties.variant` | AB variant | `{{ properties.variant }}` | "books" |
| `properties.clicks` | Variant clicks | `{{ properties.clicks }}` | 11 |

4. Click **Save**

**Result:** When a `Surprise Clicked` event fires in Segment, LaunchDarkly receives:
```json
{
    "Event Name": "Surprise Clicked",
    "Email": "agvbsdbrtf@example.com",
    "Context Kind": "user",
    "AB variant": "books",
    "Variant clicks": 11
}
```

**Step 4: Create Metrics in LaunchDarkly**
1. In LaunchDarkly, go to **Metrics** → **Create metric**
2. Create a metric with these settings:
   - **Name**: "Surprise Button Clicks"
   - **Event kind**: Custom
   - **Event name**: `Surprise Clicked` (MUST match Segment event name exactly)
   - **Metric type**: Custom conversion (count)
   - **Success criteria**: Higher is better
3. Click **Save metric**

**Step 5: Attach Metric to Experiment**
1. Go to your `dynamic-content-widget` flag
2. Click **Experiments** tab → **Create experiment**
3. Select your "Surprise Button Clicks" metric
4. Set hypothesis: "Fun facts increase engagement vs books"
5. Click **Start recording**

**Step 6: Verify Integration**
1. Interact with the app (click "Surprise Me!" button)
2. Check Segment **Debugger** - you should see `Surprise Clicked` events
3. Check LaunchDarkly **Metrics** dashboard - events should appear within 1-2 minutes
4. View experiment results showing click rates per variation

**Important Field Mapping Rules:**
- ✅ Segment `event name` MUST exactly match LaunchDarkly `metric event key`
- ✅ Segment `userId` or `anonymousId` must match LaunchDarkly context key
- ✅ In this project: `Surprise Clicked` event → `Surprise Clicked` metric
- ✅ Track events include properties like `variant` and `clicks` for richer analysis

### 5. Run the Application

```bash
# Option 1: Using Flask directly (development)
python app.py

# Option 2: Using Gunicorn (production-like)
gunicorn --bind=0.0.0.0:5000 --reuse-port app:app
```

The app will be available at: **http://localhost:5000**

You can now use it the same way as described in the "How to Use the Live Demo" section above!

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

**Data Flow:**
```
User clicks "Surprise Me!" 
  → Segment tracks event: "Surprise Clicked" with {variant: "books", clicks: 3}
  → Event sent to LaunchDarkly (Actions) destination
  → LaunchDarkly metric receives event
  → Experiment dashboard updates with results per variation
  → You see which variant (books vs fun-facts) drives more engagement!
```

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
