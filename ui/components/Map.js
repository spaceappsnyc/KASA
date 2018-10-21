import React, { Component } from 'react';
import { View, Text } from 'react-native';
import { MapView } from 'expo';

const Marker = MapView.Marker

export default class Map extends Component {
    constructor(props) {
      super(props);  
      this.state = {
        latitude: 7.247324,
        longitude: 6.010124,
        error:null,
        concat: null,
        coords: [],
        cordLatitude: this.props.startLatitude,
        cordLongitude: this.props.startLongitude,
      };
    }

  renderMarkers() {
    return this.props.places.map((place, i) => (
      <Marker key={i} title={place.nearbyIdpCamp} coordinate={place.coords} />
    ))
  }

  render() {
    const { region } = this.props
    return (
      <MapView
        style={styles.container}
        region={region}
        showsUserLocation
        showsMyLocationButton
      >
        {this.renderMarkers()}
      </MapView>
    )
  }
}
const styles = {
  container: {
    width: '100%',
    height: '40%',
  }
}