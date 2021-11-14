import { Fragment, useEffect, useState } from 'react';
import ReactDOM from 'react-dom';

import classes from 'style-loader!css-loader?modules!./Modal.module.css';

const Backdrop = (props) => {
    return <div className={classes.backdrop} onClick={props.onClose}/>
};

const ModalOverlay = (props) => {
    return (
    <div className={classes.modal}>
        <div className={classes.content}>{props.children}</div>
    </div>
    );
};

const portalElement = document.getElementById('overlays');


const Modal = (props) => {
    const [domReady, setDomReady] = React.useState(false);
    React.useEffect(() => {
        setDomReady(true);
    })
    return (
    domReady ?
    (
    <Fragment>
        {ReactDOM.createPortal(<Backdrop onClose={props.onClose} />, portalElement)}
        {ReactDOM.createPortal(<ModalOverlay>{props.children}</ModalOverlay>,
         portalElement
         )}
    </Fragment>
    ) : null
    );
};

export default Modal;