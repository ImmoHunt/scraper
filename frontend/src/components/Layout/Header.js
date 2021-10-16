import React, { Fragment } from 'react';

//import HeaderCartButton from './HeaderCartButton';
import mealsImage from 'file-loader!../../assets/meals.jpg';
import classes from 'style-loader!css-loader?modules!./Header.module.css';



const Header = (props) => {
    return (
    <Fragment>
        <header className={classes.header}>
            <h1>ReactMeals</h1>
            <button>Cart</button>
            //<HeaderCartButton onClick={props.onShowCart} />
        </header>
        <div className={classes['main-image']}>
            <img src={mealsImage} alt='A mesa cheia da comida deliciosa!' />
        </div>
    </Fragment>
    );
};

export default Header;