import React from 'react';
import { Text, SafeAreaView, StyleSheet } from 'react-native';
import { Button } from 'react-native-elements';
import FlatListBasics from '../components/List';

export default class DetailsScreen extends React.Component {
  static navigationOptions = {
    title: 'Details',
  };

  state = { }

  render() {
    return (
      <SafeAreaView style={styles.container}>
       
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



