# mentor_matching
The project is created as per requierments for TECH7009. This work belongs to Bijay Shrestha.

The Frontend and Backend Folder contains respective programs.

The frontend of webapp is built using REACT JS and can be installed using following commands.

Getting Started with Create React App

This project was bootstrapped with Create React App.

Available Scripts

Firstly run

npm install

Then, in the project directory, you can run:

npm start

Runs the app in the development mode.
Open http://localhost:3000 to view it in your browser.

The page will reload when you make changes.
You may also see any lint errors in the console.

npm test

Launches the test runner in the interactive watch mode.
See the section about running tests for more information.

npm run build

Builds the app for production to the build folder.
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.
Your app is ready to be deployed!

See the section about deployment for more information.

npm run eject

Note: this is a one-way operation. Once you eject, you can't go back!

If you aren't satisfied with the build tool and configuration choices, you can eject at any time. This command will remove the single build dependency from your project.

Instead, it will copy all the configuration files and the transitive dependencies (webpack, Babel, ESLint, etc) right into your project so you have full control over them. All of the commands except eject will still work, but they will point to the copied scripts so you can tweak them. At this point you're on your own.

You don't have to ever use eject. The curated feature set is suitable for small and middle deployments, and you shouldn't feel obligated to use this feature. However we understand that this tool wouldn't be useful if you couldn't customize it when you are ready for it.

Learn More

You can learn more in the Create React App documentation.

To learn React, check out the React documentation.

Code Splitting

This section has moved here: https://facebook.github.io/create-react-app/docs/code-splitting

Analyzing the Bundle Size

This section has moved here: https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size

Making a Progressive Web App

This section has moved here: https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app

Advanced Configuration

This section has moved here: https://facebook.github.io/create-react-app/docs/advanced-configuration

Deployment

This section has moved here: https://facebook.github.io/create-react-app/docs/deployment

npm run build fails to minify

This section has moved here: https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify



Backend:

The first thing to do is to clone the repository:

$ git clone https://github.com/gocardless/mentor_matching.git $ cd mentor_matching Create a virtual environment to install dependencies in and activate it:

$ virtualenv2 --no-site-packages env $ source env/bin/activate Then install the dependencies:

(env)$ pip install -r requirements.txt Note the (env) in front of the prompt. This indicates that this terminal session operates in a virtual environment set up by virtualenv2.

Once pip has finished downloading the dependencies:

(env)$ cd project (env)$ python manage.py runserver And navigate to http://127.0.0.1:8000/mentor_matching/.

In order to test the purchase flows, fill in the account details in project/gc_app/views.py to match your SANDBOX developer credentials.
