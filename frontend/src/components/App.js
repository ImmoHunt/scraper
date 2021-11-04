import { Fragment, useState } from 'react';

import Header from './Layout/Header';
import Meals from './Meals/Meals';
import Cart from './Cart/Cart';

function App() {
  return (
    <Fragment>
      <Header />
      <main>
        <Meals />
      </main>
    </Fragment>
  );
}
export default App;
