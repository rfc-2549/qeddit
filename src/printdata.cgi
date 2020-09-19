#!/usr/bin/perl

use JSON;
use LWP::UserAgent;
use CGI;

my $q = CGI->new;
my $ua = LWP::UserAgent->new;
my $JSON = JSON->new;
$ua->agent("Mozilla/5.0 (Windows NT 10.0; WOW64; rv:74.0.1) Gecko/20100101 Firefox/74.0.1");

my $destination = $q->param("destination");
print $q->header;
print "<style>
#rowContainer {
  width: 1240px;
  height: auto;
  display: flex;
  align-items: stretch;
  justify-content: space-between;
  margin: 0 auto;
}
#post {
  height: 254px;
  width: 204px;
  background-color: #bebebe;
  text-align: center;
  padding: 2px;
  float: left;
}
img{
  font-size: 100px;
  max-height: 125px;
  max-width: 200px;
  color: #bebebe;
  position: relative;
  top: 50%;
  transform: translateY(-50%);
  display: inline-block;
}
#image {
  height: 125px;
  width: 100%;
  background-color: #383c4a;
  position: relative;
}
a {
  text-decoration: none;
 }
#cText {
  height: 129px;
  background-color: #404552;
  overflow: hidden;
}
#cText a {
  color: #327d56;
}
#title {
  height: 91px;
  background-color: #404552;
  overflow-y: auto;
  overflow-x: hidden;
  text-decoration: none;
}

body {
  background-color: #2f343f;
  color: #bebebe;

</style>";

print $q->h1("r/".$destination);
my $json_data = $JSON->decode($ua->get("https://old.reddit.com/r/$destination/.json?&limit=20")->content);
for (my $i = 0; $i<20;$i++) {
  my $title = $json_data->{data}->{children}->[$i]->{data}->{title};
  my $author = $json_data->{data}->{children}->[$i]->{data}->{author};
  my $content = $json_data->{data}->{children}->[$i]->{data}->{selftext_html};
  my $url = $json_data->{data}->{children}->[$i]->{data}->{url};
  my $proxy_url = "proxy.cgi?url=$url";
  my $is_image;

  if ($url =~ /.*(jpg|png)/i) {
    $is_image = 1;
  }
  if($i % 5 == 0) {
    if($x > 0)
      {
	print "</div>\n<p />";
      }
  }
  print "<div id='post'>\n";
  print "<div id='image'><a href='$url'><img src='$proxy_url' alt='TXT'></a></div>";
  print "<div id='title'>$title</div>\n";
  print "A:$author\n";
  print "</div>\n</div>\n";
  }
