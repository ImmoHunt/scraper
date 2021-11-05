import { Fragment, useState } from 'react';

import Header from './Layout/Header';
import Meals from './Meals/Meals';

function App() {
  return (
    <Fragment>
      <Cart />
      <Header />
      <main>
        <Meals />
      </main>
    </Fragment>
  );
}
export default App;
