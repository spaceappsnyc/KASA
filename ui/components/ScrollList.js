import React, { Component } from 'react'
import { Badge } from 'react-native-elements';
import { Text, View, TouchableOpacity, StyleSheet, ScrollView, Modal } from 'react-native'
import data from '../assets/camp_info.json';
import PopupDialog from 'react-native-popup-dialog';
   
class ScrollList extends Component {
  state = {
    isModalOpen: false
  }

   handleCampChoice = (item) => {
      this.setModalVisible(!this.state.modalVisible);
   }

   setModalVisible(visible) {
    this.setState({modalVisible: visible});
  }

   render() {
      return (
        <ScrollView>
         <View>
            {
               this.props.camps.map((item, index) => (
                  <TouchableOpacity
                     key = {(item.idpCamp ? item.idpCamp : item.nearbyIdpCamp)}
                     style = {styles.container}
                     onPress = {() => this.handleCampChoice(item.idpCamp)}>
                     <Text style = {styles.text}>
                        {(item.idpCamp ? `${index+1}. ${item.idpCamp}` : item.nearbyIdpCamp)}
                     </Text>
                     <Badge containerStyle={styles.badge}>
                            <Text>{item.score/10}%</Text>
                        </Badge>
                  </TouchableOpacity>
               ))
            }
         </View>
         </ScrollView>
      )
   }
}
export default ScrollList

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