# coding=utf-8
u"A Nodel event receiver that emits a Google Analytics event."

from pyga.requests import Tracker, Page, Session, Visitor

# Configuration
# One or more UA-xxxx accounts
# Default type of event to log eg: pageview, play event

param_domain = Parameter('{ "name": "domain", "schema": {"type": "string"}, "value": "example.com" }')
param_tracking_id = Parameter('{ "name": "tracking_id", "schema": {"type": "string"}, "value": "UA-xxxxxxxx" }')
param_default_event = Parameter('{ "name": "default_event", "schema": {"type": "string"}, "value": "pageview" }')


def local_action_Track(args = None):
  '''{ "title": "Track", "desc": "Track a Google Analytics event."}'''

  if not 'type' in args or args['type'] == 'pageview':
    _track_pageview(args)

"""
  Page view requires an URL and an ip address
"""
def _track_pageview(args):
  tracker = Tracker(param_tracking_id, param_domain)
  visitor = Visitor()
  visitor.ip_address = args.ip_address
  session = Session()
  page = Page(args.url)
  tracker.track_pageview(page, session, visitor)


"""
  Represents an Event
  https://developers.google.com/analytics/devguides/collection/gajs/eventTrackerGuide
  Properties:
  category -- The general event category
  action -- The action for the event
  label -- An optional descriptor for the event
  value -- An optional value associated with the event. You can see your
           event values in the Overview, Categories, and Actions reports,
           where they are listed by event or aggregated across events,
           depending upon your report view.
  noninteraction -- By default, event hits will impact a visitor's bounce rate.
                    By setting this parameter to true, this event hit
                    will not be used in bounce rate calculations.
                    (default False)
"""
def _track_event(args):
  tracker = Tracker(param_tracking_id, param_domain)
  visitor = Visitor()
  visitor.ip_address = args.ip_address
  session = Session()
  event = {
    category: args['category'],
    action:   args['action'],
    label:    args['label'],
    value:  args['value']
  }
  tracker.track_event(event, session, visitor)


def main(arg = None):
  print 'Main sequencer started.'
