import React from 'react';
import { Text, SafeAreaView, StyleSheet } from 'react-native';
import Map from '../components/Map'
import FlatListBasics from '../components/List';
import spaceAppsSerivce from '../util/spaceAppsServce';
import axios from 'axios';

const region = {
  latitude: 7.247324,
  longitude: 6.010124,
  latitudeDelta: 0.3,
  longitudeDelta: 0.3
}

export default class EmergencyScreen extends React.Component {
  static navigationOptions = {
    title: 'Top IDP Camps Near You',
  };
  state = {
    location: null,
    region: null,
    startLatitude: null,
    startLongitude: null,
    error:null,
    coords: [],
    camps: [
      {
        "city": "Abuja",
        "score": 89,
        "nearbyIdpCamp": "New Kuchingoro IDP Camp",
        "coords": {
            "latitude": 9.0141174,
            "longitude": 7.3495535
        }
    }, {
        "city": "Abuja",
        "score": 89,
        "nearbyIdpCamp": "Kuje IDP Camp",
        "coords": {
            "latitude": 9.0543071,
            "longitude": 7.25427
        }
    }, {
        "city": "Lagos",
        "score": 76,
        "nearbyIdpCamp": "Lagos IDP Camp",
        "coords": {
            "latitude": 6.4932649,
            "longitude": 3.6544819
        }
    }, {
        "city": "Maiduguri",
        "score": 58,
        "nearbyIdpCamp": "Teachers Village IDP Camp",
        "coords": {
            "latitude": 11.8585332,
            "longitude": 13.1781123
        }
    }, {
        "city": "Maiduguri",
        "score": 58,
        "nearbyIdpCamp": "National Youth Service Scheme IDP Camp",
        "coords": {
            "latitude": 11.840812,
            "longitude": 13.0615935
        }
    }, 
    ]
  }

  setStartCoords = (lat) =>{
    this.setState({
      startLatitude: lat.lat,
      startLongitude: lat.long
    })
  }

  render() {
    return (
      <SafeAreaView style={styles.container}>
        <Map
          region={region}
          places={this.state.camps}
          destLatitude={this.state.startLatitude}
          destLongitude={this.state.startLongitude}
        />
        <FlatListBasics 
        camps={this.state.camps}
        setStartCoords={this.setStartCoords} 
        />
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
