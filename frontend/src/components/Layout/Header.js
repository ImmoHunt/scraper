import React, { Fragment } from 'react';

import HeaderCartButton from './HeaderCartButton';
import classes from 'style-loader!css-loader?modules!./Header.module.css';



const Header = (props) => {
    return (
    <Fragment>
        <header className={classes.header}>
            <h1>ReactMeals</h1>
            <HeaderCartButton onClick={props.onShowCart} />

        </header>
        <div className={classes['main-image']}>
        <img src={"../../../../static/frontend/meals.jpg"} alt='A mesa cheia da comida deliciosa!' />
        </div>
    </Fragment>
    );
};

export default Header;