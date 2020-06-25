import React from 'react';
import './App.css';
import {
    BrowserRouter as Router, Switch, Route
} from "react-router-dom";
import {Connections} from "./components/Connections";

function App() {
    return (
        <div className="App">
            <Router>
                <Switch>
                    <Route path="">
                        <Connections/>
                    </Route>
                </Switch>
            </Router>
        </div>
    );
}

export default App;
