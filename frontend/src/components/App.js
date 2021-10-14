import React, { Component } from "react";
import { render } from "react-dom";

const App = () => {
    return (
        <div>
        <h1>bem vindo</h1>
        <h2>Aqui temos uma nova realidade</h2>
        </div> );
}

export default App;

const container = document.getElementById("app");
render(<App />, container);