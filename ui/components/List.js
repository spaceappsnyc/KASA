import React, { Component } from 'react'
import { Badge } from 'react-native-elements';
import { Text, View, TouchableOpacity, StyleSheet } from 'react-native'
   
class List extends Component {
   state = {
      names: [
         {
            id: 0,
            name: '1. Lughe IDP Camp',
         },
         {
            id: 1,
            name: '2. Kuge IDP Camp',
         },
         {
            id: 2,
            name: '3. Area One IDP Camp',
         },
         {
            id: 3,
            name: '4. New Kuchingoro IDP Camp',
         },
         {
            id: 4,
            name: '5. Bakassi IDP camp',
         }
      ]
   }
   alertItemName = (item) => {
      alert(item.name)
   }
   render() {
      return (
         <View>
            {
               this.state.names.map((item, index) => (
                  <TouchableOpacity
                     key = {item.id}
                     style = {styles.container}
                     onPress = {() => this.alertItemName(item)}>
                     <Text style = {styles.text}>
                        {item.name}
                     </Text>
                     <Badge containerStyle={styles.badge}>
                            <Text>97%</Text>
                        </Badge>
                  </TouchableOpacity>
               ))
            }
         </View>
      )
   }
}
export default List

const styles = StyleSheet.create ({
   container: {
      flex: 0,
      flexDirection: 'row',
      padding: 20,
      marginTop: 3,
      backgroundColor: '#F8F8FF',
      alignItems: 'center',
   },
   text: {
      color: '#4f603c'
   },
   badge: {
    backgroundColor: 'lightgreen',
    marginLeft: 20,
   }
})