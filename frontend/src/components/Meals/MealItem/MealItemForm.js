import { useRef, useState } from 'react';

import Input from '../../UI/Input';

import classes from 'style-loader!css-loader?modules!./MealItemForm.module.css';

const MealItemForm = props => {
    const [amountIsValid, setAmountIsValid]= useState(true);

    const amountInputRef = useRef();

    const submitHandler = event => {
        event.preventDefault();

        const enteredAmount = amountInputRef.current.value;
        const enteredAmountNumber = +enteredAmount;

        if(enteredAmount.trim().length === 0 || enteredAmountNumber < 1 || enteredAmountNumber > 5) {
            setAmountIsValid(false);
            return;
        }

        props.onAddToCart(enteredAmountNumber);
    };
    return <form className={classes.form} onSubmit={submitHandler}>
        <Input label="Amount" input={{
            ref: {amountInputRef},
            id: 'amount',
            type: 'number',
            min: '1',
            max: '5',
            step: '1',
            defaultValue: '1'
        }}></Input>
        <button>+ Add</button>
        {!amountIsValid && <p>Please enter a valid amount (1-5).</p>}
    </form>


};

export default MealItemForm;