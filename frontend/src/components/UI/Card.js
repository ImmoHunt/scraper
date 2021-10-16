import classes from 'style-loader!css-loader?modules!./Card.module.css';

const Card = props => {
    return <div className={classes.card}>{props.children}</div>
};

export default Card;