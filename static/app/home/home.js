import $ from 'jquery';
import render from '../render';
import template from './home.handlebars';
import tweetsTemplate from './tweets.handlebars';
import loadingTemplate from './loading.handlebars';
import search from './tweets.js';

const loading = () => $('#tweets').html(loadingTemplate());
const renderList = (tweets) => $('#tweets').html(tweetsTemplate(tweets));

const initializeHome = () => {
  $('#search').submit(e => {
    e.preventDefault();
    loading();
    search($('#search-input').val())
      .then(tweets => renderList(tweets));
  });
};

const home = () => {
  render(template());
  initializeHome();
};


export default home;
