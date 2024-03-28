// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  "measurementId": "AIzaSyDRvScA5Y0LOSf6m4aEzzwYGkvEGieZozQ",
  "appId": "csc-196p-poc-proj01-rfid-1e750.firebaseapp.com",
  "storageBucket":
    "https://csc-196p-poc-proj01-rfid-1e750-default-rtdb.firebaseio.com",
  "messagingSenderId": "csc-196p-poc-proj01-rfid-1e750",
  "projectId": "csc-196p-poc-proj01-rfid-1e750.appspot.com",
  "databaseURL": "300929228398",
  "authDomain": "1:300929228398:web:910b784cb545f0ca12d07f",
  "apiKey": "G-1JNT464R05",
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);
