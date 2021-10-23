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

        </div>
    </Fragment>
    );
};

export default Header;