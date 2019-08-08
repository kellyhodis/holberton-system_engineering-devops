exec {"/usr/bin/env sudo apt-get -y update": }
exec {"/usr/bin/env sudo apt-get -y install nginx": }
exec {"/usr/bin/env sudo service nginx start": }
exec {'/usr/bin/env echo "Holberton School" > /var/www/html/index.nginx-debian.html': }
exec {'/usr/bin/env new_string="}\n\n\trewrite ^\/redirect_me intranet.hbtn.io permanent;\n"': }
exec {'/usr/bin/env sudo sed -i "0,/}/s//$new_string/" /etc/nginx/sites-enabled/default': }
exec {'/usr/bin/env echo "Ceci n\'est pas une page" > /var/www/html/404.html': }
exec {'/usr/bin/env new_error_string="}\n\n\terror_page 404 \/404.html;\n"': }
exec {'/usr/bin/env sudo sed -i "0,/}/s//$new_error_string/" /etc/nginx/sites-enabled/default': }
exec {"/usr/bin/env sudo service nginx restart": }
