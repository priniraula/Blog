import React from 'react';
import { Link } from 'react-router-dom';

const home = () => (
    <div className='container'>
        <div className="jumbotron mt-5">
            <h1 className="display-4">Learning react: in progress</h1>
            <hr className="my-4" />
            <p>things do not work yet since they aren't connected yet</p>
            <Link className="btn btn-primary btn-lg" to='#' role="button">broken</Link>
        </div>
    </div>
);

export default home;