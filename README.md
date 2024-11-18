# IoT-Based Home Automation System

## Overview

This project implements an IoT-based home automation system using a Raspberry Pi and a React Native mobile application. The system allows users to monitor and control various aspects of their home environment, such as lighting and temperature, via a mobile app interface. The system utilizes the MQTT protocol for efficient communication between the Raspberry Pi and the mobile app.

## Features

- Monitor and control home lighting and temperature.
- Real-time data updates using the MQTT protocol.
- Mobile application interface for easy control.
- Modular and maintainable codebase with reusable components.



## Components

### Raspberry Pi

- **Python Scripts:** Manage sensor data collection and actuator control.
- **MQTT Protocol:** Facilitates real-time communication.

### Mobile Application

- **React Native:** Provides the UI for user interaction.
- **Axios:** Handles HTTP requests to the server.

## Installation and Setup

### Prerequisites

- **Raspberry Pi** with Raspbian OS.
- **Node.js** and **npm** for running React Native.
- **Android Studio/Xcode** for mobile app testing on simulators.

### Raspberry Pi Setup

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd HomeAutomationSystem/raspberry_pi
   ```

2. Install Python dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Update the `config.py` file with your MQTT broker details and GPIO pin numbers.

4. Run the main script:

   ```bash
   python3 main.py
   ```

### Mobile App Setup

1. Navigate to the mobile app directory:

   ```bash
   cd HomeAutomationSystem/mobile_app/app
   ```

2. Install npm dependencies:

   ```bash
   npm install
   ```

3. Update `config.js` with your server API URL.

4. Run the app:

   ```bash
   npm start
   ```

   For Android:

   ```bash
   npm run android
   ```

   For iOS (macOS only):

   ```bash
   npm run ios
   ```

## Usage

- Use the app to view real-time sensor data on temperature, humidity, and lighting.
- Toggle home lighting using the mobile app interface.
- Ensure the Raspberry Pi is connected to the same network as your mobile device for seamless communication.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any improvements or feature additions.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Future Improvements

- Add support for voice commands using an API like Google Assistant or Alexa.
- Expand the system to include more sensors and actuators.
- Implement enhanced security features for remote access.

## Contact

For questions or support, reach out to [Your Name] at [your.email@example.com].

```

---
