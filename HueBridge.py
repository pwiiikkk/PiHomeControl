#!/usr/bin/python

import config
import logging
import phue
import json

global _bridge
_bridge = None


def _checkBridge():
    global _bridge
    if _bridge is None and config.hueBridgeIP is not None:
            _bridge = phue.Bridge(ip=config.hueBridgeIP, username=config.hueAppID)


def sendCommand(lights, command):
    global _bridge
    logging.info(str(lights) + " -> " + str(command))
    try:
        _checkBridge()
        if _bridge is None:
            logging.error("  Error - HueBridge::sendCommand: No Bridge Available")
        else:
            logging.info(" <- " + json.dumps(_bridge.set_light(lights, command)))
    except Exception, e:
        logging.error("  Error - HueBridge::sendCommand: " + str(e))


def sendCommandToGroup(group, command):
    global _bridge
    logging.info("[G" + str(group) + "] -> " + str(command))
    try:
        _checkBridge()
        if _bridge is None:
            logging.error("  Error - HueBridge::sendCommand: No Bridge Available")
        else:
            logging.info(" <- " + json.dumps(_bridge.set_group(group, command)))
    except Exception, e:
        logging.error("  Error - HueBridge::sendCommandToGroup: " + str(e))


def turnLightsOff(lights):
    global _bridge
    logging.info(str(lights) + " -> " + str(config.lightCommands.get("Off")))
    try:
        _checkBridge()
        if _bridge is None:
            logging.error("  Error - HueBridge::sendCommand: No Bridge Available")
        else:
            logging.info(" <- " + json.dumps(_bridge.set_light(lights, config.lightCommands.get("Off"))))
    except Exception, e:
        logging.error("  Error - HueBridge::turnLightsOff: " + str(e))
