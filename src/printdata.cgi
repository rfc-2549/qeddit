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
print $q->h1("r/".$destination);
my $json_data = $JSON->decode($ua->get("https://old.reddit.com/r/$destination/.json?&limit=20")->content);
for (my $i = 0; $i<20;$i++) {
  my $link =$json_data->{data}->{children}->[$i]->{data}->{permalink};
  $link =~ s/\///;
  print "<a href='/redditclient/printpost.cgi?post=$link'>$json_data->{data}->{children}->[$i]->{data}->{title}</a>" . "<br/>";
}
