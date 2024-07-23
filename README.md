# Digital Marketing Dashboard

## Overview

This project is a digital marketing dashboard that integrates various data sources such as Google Analytics, Twitter, Facebook, and Instagram. The dashboard provides an interface for users to view and export data, manage their profile, and receive notifications about important updates.

## Project Structure

digital_marketing_dashboard/
│
├── app.py
├── config.py
├── requirements.txt
├── README.md
│
├── templates/
│ ├── index.html
│ ├── login.html
│ ├── register.html
│ ├── notifications.html
│ ├── profile.html
│ ├── settings.html
│
├── static/
│ ├── styles.css
│
├── models/
│ ├── user.py
│
├── routes/
│ ├── auth.py
│ ├── dashboard.py
│ ├── profile.py
│ ├── settings.py
│ ├── export.py
│
└── services/
├── google_analytics.py
├── twitter.py
├── facebook.py
├── instagram.py


## Setup

1. **Install Dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

2. **Configure Settings**:

    Update the `settings.json` file with your API keys and access tokens for Google Analytics, Twitter, Facebook, and Instagram.

3. **Run the Application**:

    ```bash
    python app.py
    ```

    The application will be accessible at `http://127.0.0.1:5000/`.

## Usage

- **Register and Login**:
  - Navigate to `/register` to create a new account.
  - Navigate to `/login` to log in with your credentials.

- **Dashboard**:
  - The main dashboard page can be accessed at `/dashboard/`.
  - View traffic data at `/dashboard/traffic`.
  - View social media data at `/dashboard/socialmedia`.
  - View Facebook data at `/dashboard/facebook`.
  - View Instagram data at `/dashboard/instagram`.
  - View conversion rates at `/dashboard/conversions`.

- **Settings**:
  - Update API keys and access tokens at `/dashboard/settings`.

- **Profile**:
  - View and update your profile at `/dashboard/profile`.

- **Notifications**:
  - View notifications at `/notifications`.

- **Export Data**:
  - Export traffic data at `/export/traffic`.
  - Export social media data at `/export/socialmedia`.
  - Export Facebook data at `/export/facebook`.
  - Export Instagram data at `/export/instagram`.

## Contributing

Feel free to contribute to this project by submitting a pull request. Ensure that your code adheres to the coding standards and includes appropriate tests.

## License

This project is licensed under the MIT License.
