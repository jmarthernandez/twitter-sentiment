import page from 'page';
import routes from './routes';

page('/', routes.home);
page('/about', routes.about);
page();
