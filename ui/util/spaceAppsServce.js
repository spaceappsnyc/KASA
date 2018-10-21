import axios from 'axios'

const getCamps = userLocation => {
  return api
    .get('http://127.0.0.1:5000/whereToGo', {})
    .then(res => {
            console.log(res);
        }
    )
    .catch(error => console.error(error))
}

export default {
  getCamps,
}