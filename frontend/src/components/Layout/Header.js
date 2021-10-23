import React, { Fragment } from 'react';


import classes from 'style-loader!css-loader?modules!./Header.module.css';



const Header = (props) => {
    return (
    <Fragment>
        <header className={classes.header}>
            <h1>ReactMeals</h1>
            <button>Cart</button>

        </header>
        <div className={classes['main-image']}>
        <img src={"../../../../static/frontend/meals.jpeg"} alt='A mesa cheia da comida deliciosa!' />
        </div>
    </Fragment>
    );
};

export default Header;