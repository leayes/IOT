import React from 'react';
   import { View, Text, StyleSheet } from 'react-native';

   const Header = () => {
     return (
       <View style={styles.headerContainer}>
         <Text style={styles.headerText}>Home Automation App</Text>
       </View>
     );
   };

   const styles = StyleSheet.create({
     headerContainer: {
       padding: 20,
       backgroundColor: '#4CAF50',
       alignItems: 'center',
     },
     headerText: {
       color: 'white',
       fontSize: 24,
       fontWeight: 'bold',
     },
   });

   export default Header;