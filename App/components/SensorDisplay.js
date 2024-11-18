  import React from 'react';
   import { View, Text, StyleSheet } from 'react-native';

   const SensorDisplay = ({ temperature, humidity, lighting }) => {
     return (
       <View style={styles.sensorContainer}>
         <Text style={styles.sensorText}>Temperature: {temperature}°C</Text>
         <Text style={styles.sensorText}>Humidity: {humidity}%</Text>
         <Text style={styles.sensorText}>Lighting: {lighting}%</Text>
       </View>
     );
   };

   const styles = StyleSheet.create({
     sensorContainer: {
       marginBottom: 20,
     },
     sensorText: {
       fontSize: 18,
     },
   });

   export default SensorDisplay;