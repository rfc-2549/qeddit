#!/usr/bin/perl

use JSON;
use LWP::UserAgent;
use CGI;
my $q = CGI->new;
my $ua = LWP::UserAgent->new;
my $JSON = JSON->new;
$ua->agent("Mozilla/5.0 (Windows NT 10.0; WOW64; rv:74.0.1) Gecko/20100101 Firefox/74.0.1");
print $q->header;
my $post = $q->param("post");
my $json_data = $JSON->decode($ua->get("https://old.reddit.com/$post/.json")->content);
my $num_comments = $json_data->[0]->{data}->{children}->[0]->{data}->{num_comments};
print $q->h2($json_data->[0]->{data}->{children}->[0]->{data}->{title});
my $post = $json_data->[0]->{data}->{children}->[0]->{data}->{selftext_html};
my $post_img = $json_data->[0]->{data}->{children}->[0]->{data}->{url_overridden_by_dest};

print "<img src=\"$post_img\" alt=\"image\"/>" if $post_img;

$post =~ s/&gt;/>/g;
$post =~ s/&lt;/</g;
print $post;

print $q->h3("comments");

for (my $i = 1;$i<$num_comments;$i++) {
  print "<b>$json_data->[1]->{data}->{children}->[$i]->{data}->{author} :</b>  ";
  print $json_data->[1]->{data}->{children}->[$i]->{data}->{body};
  print "<br/><br/>";

}
