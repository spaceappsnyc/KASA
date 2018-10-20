import React from 'react';
import { Text, SafeAreaView, StyleSheet } from 'react-native';
import Map from '../components/Map'
import FlatListBasics from '../components/List';

const region = {
  latitude: 6.465422,
  longitude: 3.406448,
  latitudeDelta: 0.0922,
  longitudeDelta: 0.0421
}

export default class EmergencyScreen extends React.Component {
  static navigationOptions = {
    title: 'Emergency',
  };
  state = {
    region: null,
    camps: []
  }

  render() {
    return (
      <SafeAreaView style={styles.container}>
        <Map
          region={region}
          places={this.state.camps}
        />
        <FlatListBasics ></FlatListBasics>
      </SafeAreaView>
    );
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    flexDirection: 'column',
    backgroundColor: '#fff',
  }
})



