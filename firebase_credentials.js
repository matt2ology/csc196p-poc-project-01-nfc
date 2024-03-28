// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyDRvScA5Y0LOSf6m4aEzzwYGkvEGieZozQ",
  authDomain: "csc-196p-poc-proj01-rfid-1e750.firebaseapp.com",
  databaseURL:
    "https://csc-196p-poc-proj01-rfid-1e750-default-rtdb.firebaseio.com",
  projectId: "csc-196p-poc-proj01-rfid-1e750",
  storageBucket: "csc-196p-poc-proj01-rfid-1e750.appspot.com",
  messagingSenderId: "300929228398",
  appId: "1:300929228398:web:910b784cb545f0ca12d07f",
  measurementId: "G-1JNT464R05",
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);
