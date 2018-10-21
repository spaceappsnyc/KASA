import React, { Component } from 'react'
import { Badge } from 'react-native-elements';
import { Text, View, TouchableOpacity, StyleSheet, ScrollView, Modal, TouchableHighlight, Button } from 'react-native'
import data from '../assets/camp_info.json';
import PopupDialog from 'react-native-popup-dialog';
   
class ScrollList extends Component {
  state = {
    modalVisible: false,
    data: {}
  }

   handleCampChoice = (item) => {
      this.setModalVisible(true);
      this.setState({data: data[item]});
   }

   setModalVisible(visible) {
    this.setState({modalVisible: visible});
  }

   render() {
     console.log(this.state.data);
      return (
        <View>
        <ScrollView>
          <Modal
          animationType="slide"
          transparent={false}
          visible={this.state.modalVisible}
          onRequestClose={() => { Alert.alert('Modal has been closed.'); }}>
          <View style={{
            flex: 1,
            flexDirection: 'column',
            justifyContent: 'center',
            alignItems: 'center'}}>
            <View style={{
              width: 300,
              height: 300}}>
              <Text>
                {
                  Object.keys(this.state.data).map((item) => {
                    const upper = item.charAt(0).toUpperCase() + item.substr(1);
                    return upper + ': ' + this.state.data[item] + '\n';
                  })
                }
              </Text>

              <Button 
                title="Hide Modal"
                onPress={() => {
                  this.setModalVisible(!this.state.modalVisible);
                }}>
                </Button>
            </View>
            </View>
            </Modal>
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
         </ScrollView>
         </View>
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
   },

})