  import React from 'react';
   import { Button, Alert } from 'react-native';

   const ToggleButton = ({ isLightOn, onToggle }) => {
     const handlePress = () => {
       onToggle();
     };

     return (
       <Button
         title={`Turn Light ${isLightOn ? 'Off' : 'On'}`}
         onPress={handlePress}
       />
     );
   };

   export default ToggleButton;