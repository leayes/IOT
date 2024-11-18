import { StatusBar } from 'expo-status-bar';
import React, { useState, useEffect } from 'react';
import { View, ActivityIndicator, Alert, StyleSheet } from 'react-native';
import { API_URL } from './config';
import Header from './components/Header';
import SensorDisplay from './components/SensorDisplay';
import ToggleButton from './components/ToggleButton';

const App = () => {
  const [sensorData, setSensorData] = useState(null);
  const [isLoading, setIsLoading] = useState(true);
  const [isLightOn, setIsLightOn] = useState(false);

  useEffect(() => {
    fetchSensorData();
  }, []);

  const fetchSensorData = () => {
    fetch(`${API_URL}/sensors`)
      .then(response => response.json())
      .then(data => {
        setSensorData(data);
        setIsLoading(false);
      })
      .catch(error => {
        console.error('Error fetching sensor data:', error);
        Alert.alert('Error', 'Unable to fetch sensor data.');
        setIsLoading(false);
      });
  };

  const controlLights = () => {
    fetch(`${API_URL}/control`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ command: 'toggle_light' }),
    })
    .then(response => response.json())
    .then(data => {
      if (data.success) {
        Alert.alert('Success', 'Light toggled successfully.');
        setIsLightOn(prevState => !prevState);
      } else {
        Alert.alert('Failure', 'Failed to toggle light.');
      }
    })
    .catch(error => {
      console.error('Error toggling light:', error);
      Alert.alert('Error', 'Unable to toggle light.');
    });
  };

  return (
    <View style={styles.container}>
      <Header />
      {isLoading ? (
        <ActivityIndicator size="large" color="#0000ff" />
      ) : (
        <SensorDisplay
          temperature={sensorData?.temperature || 'N/A'}
          humidity={sensorData?.humidity || 'N/A'}
          lighting={sensorData?.lighting || 'N/A'}
        />
      )}
      <ToggleButton isLightOn={isLightOn} onToggle={controlLights} />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    padding: 16,
    backgroundColor: '#f5f5f5',
  },
});

export default App;