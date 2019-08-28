import firebase from '@firebase/app'
import '@firebase/auth'
import '@firebase/firestore'

firebase.initializeApp({
  apiKey: "AIzaSyDNiDw8Z-zDqRUQoe7-pVNvahQaVyWGYnE",
  authDomain: "hack-to-h.firebaseapp.com",
  databaseURL: "https://hack-to-h.firebaseio.com",
  projectId: "hack-to-h",
  storageBucket: "",
  messagingSenderId: "78199436159",
  appId: "1:78199436159:web:8f1c8ef382fbebbf"
});

export default firebase