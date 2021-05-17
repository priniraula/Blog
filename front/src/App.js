import React from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';

import Layout from './highercomponents/Layout';

import Home from './components/Home';
import Blog from './components/Blog';
import BlogDetail from './components/BlogDetail';

const App = () => (
    <BrowserRouter>
        <Layout>
            <Switch>
                <Route exact path='/' component={Home} />
                <Route exact path='/blog' component={Blog} />
                <Route exact path='/blog/:id' component={BlogDetail} />
            </Switch>
        </Layout>
    </BrowserRouter>
);

export default App;