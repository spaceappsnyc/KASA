import React, { Component } from 'react'
import { Badge } from 'react-native-elements';
import { Text, View, TouchableOpacity, StyleSheet } from 'react-native'
   
class List extends Component {
   handleCampChoice = (item) => {
      this.props.setStartCoords({
          lat: item.coords.latitude,
          long: item.coords.longitude
      })
   }

   render() {
      return (
         <View>
            {
               this.props.camps.map((item, index) => (
                  <TouchableOpacity
                     key = {item.id}
                     style = {styles.container}
                     onPress = {() => this.handleCampChoice(item)}>
                     <Text style = {styles.text}>
                        {item.nearbyIdpCamp}
                     </Text>
                     <Badge containerStyle={styles.badge}>
                            <Text>{item.score}%</Text>
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
      justifyContent: 'space-between',
   },
   text: {
      color: '#4f603c'
   },
   badge: {
    backgroundColor: 'lightgreen',
    alignContent: 'flex-end',
   }
})