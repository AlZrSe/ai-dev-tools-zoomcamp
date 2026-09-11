# ChoreManager: Household Chore Management Tool

## Project Overview
A Vue.js web application with Supabase backend designed for 2-4 person households to manage shared chores, track completion, handle expenses, and coordinate household activities.

## Core Features

### 1. Authentication & User Management
- User registration with email/password via Supabase Auth
- Secure login/logout functionality
- Profile management (name, avatar, preferences)
- Session handling

### 2. Household System
- Create household with custom name and automatic invite code generation
- Join household via invite link or code
- Manage household members (view member list, remove members if admin)
- Leave household functionality
- Household settings management

### 3. Chore Management Core
- **Chore Creation**: 
  - Title and description fields
  - Frequency options (one-time, daily, weekly, monthly, custom)
  - Assignee selection from household members
  - Due date/time setting
  - Optional points value assignment
- **Assignment System**: 
  - Assign chores to specific household members
  - Ability to reassign chores
  - Bulk assignment options
- **Tracking**: 
  - Mark chores as complete/incomplete
  - Completion timestamps
  - Completion history per chore and per user
- **Verification** (Optional): 
  - Photo verification requirement
  - Checklist verification for multi-step chores
  - Admin approval workflow

### 4. Scheduling & Reminders
- **Calendar Views**: 
  - Monthly view with color-coded chore indicators
  - Weekly view with time-block scheduling
  - Daily view with hourly breakdown
  - List view for upcoming chores
- **Due Date Management**: 
  - Visual indicators (overdue = red, today = yellow, upcoming = green)
  - Automatic recurrence based on frequency settings
  - Snooze/reschedule functionality
- **Notification System**: 
  - Email notifications for upcoming chores (configurable timing)
  - In-app notifications
  - Browser push notifications (optional)
  - Overdue chore alerts

### 5. Points & Rewards System
- **Points Earning**: 
  - Configurable point values per chore (based on difficulty/time)
  - Bonus points for early completion
  - Streak bonuses for consistent completion
  - Penalty points for late/incomplete chores (optional)
- **Rewards System**: 
  - Customizable reward catalog (created by household admins)
  - Points redemption for rewards
  - Reward tracking and history
- **Leaderboards & Stats**: 
  - Individual points leaderboard
  - Household overall stats
  - Weekly/monthly champions
  - Achievement badges

### 6. Communication & Collaboration
- **Chore Comments**: 
  - Threaded comments on each chore
  - @mentions to notify specific household members
  - File attachment support (via Supabase Storage)
  - Edit/delete comment functionality
- **Household Communication**: 
  - Announcements board for general household messages
  - Activity feed showing recent actions (chore completions, new chores, etc.)
  - Direct messaging between household members (optional)

### 7. Expense Sharing
- **Expense Creation**: 
  - Title, description, amount, date
  - Payer selection (who paid initially)
  - Category tagging (groceries, utilities, etc.)
  - Receipt image upload (optional)
- **Split Methods**: 
  - Equal split among all household members
  - Percentage-based split
  - Custom amount split per member
  - Shares-based split (e.g., 2 shares for adults, 1 for children)
- **Tracking & Settlement**: 
  - Mark expenses as settled/pending
  - View who owes what to whom
  - Payment tracking (Venmo, CashApp, etc. integration notes)
  - Expense history and filtering
- **Integration**: 
  - Link expenses to chores (e.g., "Buy groceries" chore)
  - Automatic expense suggestions based on chore completion

### 8. Reporting & Analytics
- **Personal Dashboard**: 
  - My assigned chores (pending, completed, overdue)
  - My completed chores count and points earned
  - Upcoming chores calendar
  - My expense summary
- **Household Analytics**: 
  - Chore completion distribution by member
  - Points earned over time (individual and household)
  - Expense reports by category and time period
  - Upcoming chores heatmap
  - Completion rate trends

## Technical Architecture

### Frontend (Vue.js)
- **Framework**: Vue 3 with Composition API
- **Build Tool**: Vite for fast development and builds
- **State Management**: Pinia for centralized state
- **Routing**: Vue Router for client-side navigation
- **UI Library**: Vuetify 3 for Material Design components
- **HTTP Client**: Axios for API communication with Supabase
- **Date Handling**: date-fns for date manipulation and formatting
- **Calendar**: FullCalendar.io or Vue-Calendar for scheduling views
- **Form Handling**: VeeValidate or Vue Formulate for form validation
- **Icons**: Vuetify icons or Font Awesome

### Backend (Supabase)
- **Database**: PostgreSQL with the following tables:
  - `users`: Extends Supabase Auth users (profile info, preferences)
  - `households`: Household information (name, invite code, settings)
  - `household_members`: Junction table linking users to households (role: admin/member)
  - `chores`: Chore definitions (title, description, frequency, points, etc.)
  - `chore_assignments`: Links chores to assigned users and due dates
  - `chore_completions`: Records of chore completions (user, timestamp, verification)
  - `chore_comments`: Comment threads on chores
  - `expenses`: Expense records (payer, amount, date, description)
  - `expense_splits`: How expenses are split among household members
  - `points_transactions`: Ledger of points earned/spent
  - `notifications`: System notifications for users
  - `activity_log`: Household activity feed entries
- **Security**: Row Level Security (RLS) policies ensuring users can only access their household's data
- **Storage**: Supabase Storage for file attachments (receipt photos, verification images)
- **Edge Functions**: 
  - `process-recurring-chores`: Runs daily to create new chore instances based on frequency
  - `send-reminders`: Sends email/push notifications for upcoming chores
  - `calculate-points`: Processes point awards for completed chores
  - `generate-reports`: Creates periodic reports (optional)
- **Real-time**: Supabase Realtime for live updates (chore status changes, new comments)

## Development Approach

### Phase 1: Core Foundation (Weeks 1-2)
1. **Project Setup**:
   - Initialize Vue 3 project with Vite
   - Configure Supabase connection
   - Set up environment variables
   - Configure ESLint, Prettier, and other dev tools

2. **Authentication System**:
   - Implement Supabase Auth UI components
   - Create login/register pages
   - Add password reset functionality
   - Implement protected routes
   - Create user profile management

3. **Household Management**:
   - Create household creation form
   - Generate unique invite codes
   - Implement household joining via code/link
   - Build household member management UI
   - Add leave household functionality

4. **Basic Chore CRUD**:
   - Chore creation/edit forms
   - Chore listing and filtering
   - Assignment to household members
   - Basic completion tracking

### Phase 2: Scheduling & Engagement (Weeks 3-4)
1. **Calendar Implementation**:
   - Integrate FullCalendar.io or Vue-Calendar
   - Display chores as calendar events
   - Color-code by assignee/status
   - Add drag-and-drop rescheduling

2. **Due Dates & Reminders**:
   - Implement due date validation
   - Add visual indicators for overdue/today/upcoming
   - Create reminder configuration system
   - Set up Supabase Functions for sending reminders

3. **Points & Rewards**:
   - Design points system database schema
   - Implement points awarding on chore completion
   - Create rewards catalog management
   - Build points redemption interface

4. **Communication Features**:
   - Add comment system to chores
   - Implement @mention notifications
   - Create household announcements board
   - Build activity feed

### Phase 3: Advanced Features (Weeks 5-6)
1. **Expense Sharing System**:
   - Expense creation/form UI
   - Split calculation algorithms (equal, percentage, custom)
   - Expense listing and filtering
   - Settlement tracking

2. **Reporting & Analytics**:
   - Personal dashboard components
   - Household statistics views
   - Charts/graphs using Chart.js or Vue-Charts
   - Export functionality (CSV/PDF)

3. **Verification & Attachments**:
   - Photo upload for chore verification
   - Receipt image upload for expenses
   - File validation and storage management
   - Optional approval workflows

### Phase 4: Testing & Refinement (Weeks 7-8)
1. **User Testing**:
   - Conduct testing with 2-4 person households
   - Gather feedback on usability and features
   - Identify pain points and improvement areas

2. **Performance Optimization**:
   - Optimize database queries
   - Implement pagination for large lists
   - Add caching where appropriate
   - Bundle optimization for frontend

3. **Polish & UX Improvements**:
   - Responsive design adjustments
   - Accessibility improvements (WCAG compliance)
   - Error handling and loading states
   - Empty states and onboarding tutorials

4. **Documentation & Deployment**:
   - Create user guide/documentation
   - Write API documentation
   - Prepare deployment instructions
   - Set up CI/CD pipeline if desired

## Deployment Plan

### Hosting Options
- **Frontend**: Vercel, Netlify, or Firebase Hosting (all offer free tiers and easy Vue.js deployment)
- **Backend**: Supabase (handles database, auth, storage, and edge functions)
- **Domain**: Custom domain optional (can use Vercel/Netlify subdomain initially)

### Environment Variables
```
VITE_SUPABASE_URL=your_supabase_project_url
VITE_SUPABASE_ANON_KEY=your_supabase_anon_key
```

### Deployment Steps
1. Push code to GitHub/GitLab repository
2. Connect repository to Vercel/Netlify
3. Configure environment variables in hosting platform
4. Set up automatic deployments on main branch pushes
5. Test production deployment thoroughly
6. Monitor Supabase usage and upgrade plan if needed

## Success Criteria

### Minimum Viable Product (MVP)
- Users can register and log in securely
- Households can be created and joined via invite codes
- Chores can be created, assigned to household members, and marked as complete
- Due dates are visible and overdue chores are clearly indicated
- Basic points are awarded for chore completion
- Responsive design works on mobile and desktop

### Extended Features (Post-MVP)
- Calendar view with scheduling capabilities
- Notification system (email/in-app)
- Expense sharing with split calculations
- Communication features (comments, announcements)
- Reporting and analytics dashboard
- Rewards system and leaderboards
- Verification options (photos, checklists)

### Quality Metrics
- Page load times under 3 seconds on average
- 99% uptime for core features
- Intuitive UI requiring minimal instruction for new users
- Stable performance with up to 8 active household members
- Positive user feedback in testing (4+ out of 5 rating)

## Future Enhancements
- Integration with smart home devices (automatic chore completion triggers)
- Voice assistant compatibility (Alexa, Google Assistant)
- Gamification elements (levels, badges, challenges)
- Third-party calendar sync (Google Calendar, Apple Calendar)
- Machine learning suggestions for chore optimization
- Multi-household support (users belonging to multiple households)
- Offline functionality with sync capability