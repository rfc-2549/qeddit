#!/usr/bin/perl

use CGI;
use LWP::UserAgent;

my $q = CGI->new;
my $ua = LWP::UserAgent->new;
$ua->agent("Mozilla/5.0 (Windows NT 10.0; WOW64; rv:74.0.1) Gecko/20100101 Firefox/74.0.1");
my $url = $q->param("url");
my $jpg;
my $png;
unless($url =~ /^https:\/\/i\.redd\.it\/.*(png|jpg)/)
  {
    print $q->header;
    print "This can only proxy images from reddit\n";
    exit;
  }
print "Content-type: image/png\n\n";
print $ua->get($url)->decoded_content;
