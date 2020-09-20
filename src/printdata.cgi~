#!/usr/bin/perl

use JSON;
use LWP::UserAgent;
use CGI;
use HTML::Entities;

sub encode_uni($)
  {
    my $string = shift;
    return encode_entities($string,'^\n\x20-\x25\x26\x27-\x7e');
  }
my $q = CGI->new;
my $ua = LWP::UserAgent->new;
my $JSON = JSON->new;
$ua->agent("Mozilla/5.0 (Windows NT 10.0; WOW64; rv:74.0.1) Gecko/20100101 Firefox/74.0.1");

my $destination = $q->param("destination");
print $q->header;
print "<meta charset='utf-8'>";
print "<style>
  #rowcontainer {
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
background-color:               #bebebe;
text-align: center;
padding: 2px;
float: left;
}
  img{
    font-size: 100px;
    max-height: 125px;
    max-width: 200px;
  color:                        #bebebe;
  position: relative;
  top: 50%;
  transform: translateY(-50%);
  display: inline-block;
  }
  #image {
 height: 125px;
width: 100%;
background-color:               #383c4a;
position: relative;
}
.title_content {text-decoration:underline;}
  a {
    text-decoration: none;
  }
  #cText {
 height: 129px;
background-color:               #404552;
overflow: hidden;
}
  #cText a {
 color:                         #327d56;
}
  #title {
 height: 91px;
background-color:               #404552;
overflow-y: auto;
  overflow-x: hidden;
  text-decoration: none;
}

  body {
    background-color:           #2f343f;
  color:                        #bebebe;

    </style>";

print $q->h1("r/".$destination);
my $json_data = $JSON->decode($ua->get("https://old.reddit.com/r/$destination/.json?&limit=20")->content);
for (my $i = 0; $i<20;$i++) {
  my $title = $json_data->{data}->{children}->[$i]->{data}->{title};
  my $author = $json_data->{data}->{children}->[$i]->{data}->{author};
  my $content = $json_data->{data}->{children}->[$i]->{data}->{selftext_html};
  my $link =$json_data->{data}->{children}->[$i]->{data}->{permalink};
  # $content =~ s/&gt;/>/g; $content =~ s/&lt;/</g;
  my $url = $json_data->{data}->{children}->[$i]->{data}->{url};
  decode_entities($content);
  my $proxy_url = "proxy.cgi?url=$url";
  my $is_image;

  if ($url =~ /.*(jpg|png)/i) {
    $is_image = 1;
  }
  if ($i % 5 == 0) {
    if ($i > 0) {
      print "</div>\n";
    }
  }
  print "<div id='post'>\n";
  if ($is_image) {
    print "<div id='image'><a href='$url'><img src='$proxy_url' alt='TXT'></a></div>";
  }
  else {
     print "<div id='image'><a href='$url'>Text post, click to view</a></div>";
  }
  print "<div id='title'><a href='printpost.cgi?post=$link' class='title_content'>$title</a>\n";
  print "<p>$content</p></div>";
  print "A:$author\n";
  print "</div>\n</div>\n";
  if ($i + 1 == 20) {
    print "</div>";
  }
}
