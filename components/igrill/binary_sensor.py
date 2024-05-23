import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import binary_sensor, ble_client

from esphome.const import (
    CONF_ID,
    DEVICE_CLASS_CONNECTIVITY,
    ENTITY_CATEGORY_DIAGNOSTIC,
)

DEPENDENCIES = ["ble_client"]

igrill_ns = cg.esphome_ns.namespace("igrill")
IGrill = igrill_ns.class_(
    "IGrill", cg.PollingComponent, ble_client.BLEClientNode
)
CONF_TEMPERATURE_PROBE1_PLUGGED = "temperature_probe1_plugged"
CONF_TEMPERATURE_PROBE2_PLUGGED = "temperature_probe2_plugged"
CONF_TEMPERATURE_PROBE3_PLUGGED = "temperature_probe3_plugged"
CONF_TEMPERATURE_PROBE4_PLUGGED = "temperature_probe4_plugged"

CONFIG_SCHEMA = cv.All(
    cv.Schema(
        {
            cv.GenerateID(): cv.use_id(IGrill),
            cv.Optional(CONF_TEMPERATURE_PROBE1_PLUGGED): binary_sensor.binary_sensor_schema(
                device_class=DEVICE_CLASS_CONNECTIVITY,
                entity_category=ENTITY_CATEGORY_DIAGNOSTIC,
            ),
            cv.Optional(CONF_TEMPERATURE_PROBE2_PLUGGED): binary_sensor.binary_sensor_schema(
                device_class=DEVICE_CLASS_CONNECTIVITY,
                entity_category=ENTITY_CATEGORY_DIAGNOSTIC,
            ),
            cv.Optional(CONF_TEMPERATURE_PROBE3_PLUGGED): binary_sensor.binary_sensor_schema(
                device_class=DEVICE_CLASS_CONNECTIVITY,
                entity_category=ENTITY_CATEGORY_DIAGNOSTIC,
            ),
            cv.Optional(CONF_TEMPERATURE_PROBE4_PLUGGED): binary_sensor.binary_sensor_schema(
                device_class=DEVICE_CLASS_CONNECTIVITY,
                entity_category=ENTITY_CATEGORY_DIAGNOSTIC,
            ),
        }
    )
    .extend(cv.polling_component_schema("30s"))
    .extend(ble_client.BLE_CLIENT_SCHEMA),
)


async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)

    if CONF_TEMPERATURE_PROBE1_PLUGGED in config:
        sens = await binary_sensor.new_binary_sensor(config[CONF_TEMPERATURE_PROBE1_PLUGGED])
        cg.add(var.set_plugged_probe(sens, 1))
    if CONF_TEMPERATURE_PROBE2_PLUGGED in config:
        sens = await binary_sensor.new_binary_sensor(config[CONF_TEMPERATURE_PROBE2_PLUGGED])
        cg.add(var.set_plugged_probe(sens, 2))
    if CONF_TEMPERATURE_PROBE3_PLUGGED in config:
        sens = await binary_sensor.new_binary_sensor(config[CONF_TEMPERATURE_PROBE3_PLUGGED])
        cg.add(var.set_plugged_probe(sens, 3))
    if CONF_TEMPERATURE_PROBE4_PLUGGED in config:
        sens = await binary_sensor.new_binary_sensor(config[CONF_TEMPERATURE_PROBE4_PLUGGED])
        cg.add(var.set_plugged_probe(sens, 4))
