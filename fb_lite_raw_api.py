"""
=============================================================================
RAW CAPTURED FACEBOOK LITE v538 LOGIN API
Action: com.bloks.www.bloks.caa.login.async.send_login_request

IMPORTANT NOTICE (PLEASE READ BEFORE RUNNING):
-----------------------------------------------------------------------------
Running this script directly will NOT work out-of-the-box via standard HTTP/REST.

WHY DIRECT EXECUTION DOES NOT WORK:
1. Facebook Lite does not process authentication through standard public web
   APIs or standard REST endpoints.
2. Instead, Facebook Lite communicates through a proprietary, persistent binary
   gateway socket connection directly with Meta's backend infrastructure.
3. Every request sent by the app requires custom session handshakes, binary
   transport framing, and stateful socket management that the official Facebook
   Lite client maintains internally.
4. Sending this raw payload via a standard HTTP POST request will be rejected
   by the server because it is not being sent through an active, authenticated
   Facebook Lite gateway channel.

WHAT IS REQUIRED TO RUN THIS:
To dispatch this payload and receive valid responses, it must be routed through
one of two gateway architectures:
  • Option 1 (In-App Bridge / Device RPC): Route requests through an active,
    connected app instance that manages the gateway session natively.
  • Option 2 (Standalone Gateway Client): Build a custom binary socket engine
    that handles Meta's proprietary gateway protocol and transport framing.

-----------------------------------------------------------------------------
RESEARCH NOTICE & FULL AUTOMATION INQUIRIES:
This script is provided strictly for educational, security research, and protocol
analysis purposes. To execute this, a proper gateway system must be configured.

For full working gateway implementations, custom socket engines, or end-to-end
Facebook Lite automation solutions:
👉 Telegram: @sifathub
=============================================================================
"""

import json
import requests

# Gateway Host & Reference Endpoint
GATEWAY_HOST = "z-m-gateway.facebook.com:443"
URL = "https://b-graph.facebook.com/bloks_screen"

HEADERS = {
    "User-Agent": "FacebookLite/538.0.0.10.59 (Android 14; Mobile; x86; en_US; com.facebook.lite; Build/UDC.240811.001) [FBAN/EMA;FBLC/en_US;FBAV/538.0.0.10.59;]",
    "Accept-Language": "en-US,en;q=0.9",
    "Content-Type": "application/x-www-form-urlencoded",
    "X-FB-Connection-Type": "WIFI",
    "X-FB-Friendly-Name": "com.bloks.www.bloks.caa.login.async.send_login_request",
    "X-FB-Request-Analytics-Tags": '{"network_tags":{"product":"caa_login"}}',
    "X-FB-HTTP-Engine": "Liger",
    "X-FB-Client-IP": "True",
    "X-FB-Server-Cluster": "True",
}

# 100% Original 73-Parameter Payload
PAYLOAD = {
    "client_input_params": {
        "blocked_uids": [],
        "aac": "Q7jiDQE-zt58iVtGd2uL_0rGhaszA6lQYFpgrClCTbG3EmWPZWe4vyFK6-x-iPF0B-BkuK0e-KY85JzYKuR9sne3mW6VOgaBq-QgX1Wah-ac389wKhbdlsCvrMIlGznPPuUIEe13R3nUckHus2M7_liArRkn_M_8RgdSCW1sG_H_eeHg-XV7-or_Pr7dhJ3VweNlevMSJaa89iUDZndyKB3uURzLocT-_L1ZztbwYmq-xU8YSZ8C6UMaHlMy9uV18QMm0tSAoAHL65-1ExKoXQkkEoUN8yqH2KhGELGpKbfQRX4",
        "sim_phones": [],
        "aymh_accounts": [],
        "network_bssid": None,
        "secure_family_device_id": "647615dd-dc3a-458c-a0b3-1a17515b4a22",
        "attestation_result": {
            "keyHash": "75a7c4d28fb5d0c095a47411a0696222e8680057f6191d0ecf53a66c0bba3f11",
            "data": "eyJjaGFsbGVuZ2Vfbm9uY2UiOiJMRjRudFlJM1gwM3c2R2xyQ0VRNGVMNDZFSDhBYnhMdWtacUUyYWd6T0RVPSIsInVzZXJuYW1lIjoibXJzeHIudGVzdEBnbWFpbC5jb20ifQ=="
        },
        "has_granted_read_contacts_permissions": 1,
        "auth_secure_device_id": "",
        "has_whatsapp_installed": 0,
        "password": "#PWD_LITE4A:2:1794837793:AVLUpV7QVagdaCHNXTMAAU0Gs9wSuNKG1Ytys5e5tjM7Qa7T1di3+0szFBsUKVBbYXF6SvYnbte85gMX0SoEVCPXjGyNgvG8uVFvagxoOLmOf8lSMEu9BamHVVOCuE2YWRf0ZiLJk0hL3iI3A3sd6mWgACLTwgRo+cxniTAPBw87YRWShvyW5PxBAijuYHpXrRYgcEDAsvztiq1IK25TrZ08Ca08ArKC2x9wZld0jkSrtRPu6QDQAFbkHiJ7HQ09Yxu/IoiiE9lGY/yr65AL/p1raVHBfWDe+NrEu6rroZrzhVR8TBn5K7EWQVyUJ9JrkJEBDgcgnPLOVWlE1HknA/LOM9HtUu5JRYEI5HXKcqYltWN2DLi/tYMfLB1ESWpfW61lcEEH66+MyopzkiF88c536HXZNd2ORr80qS8AvO0=",
        "sso_token_map_json_string": "",
        "block_store_machine_id": "",
        "cloud_trust_token": None,
        "event_flow": "login_manual",
        "password_contains_non_ascii": "false",
        "sim_serials": None,
        "client_known_key_hash": "",
        "sso_accounts_auth_data": [],
        "encrypted_msisdn": "",
        "has_granted_read_phone_permissions": 0,
        "app_manager_id": "null",
        "should_show_nested_nta_from_aymh": 1,
        "device_id": 1599219345225378,
        "zero_balance_state": "skipped_due_to_wifi",
        "login_attempt_count": 1,
        "machine_id": "7cz0apG1ksxRyZqCUqfO4IZ7",
        "flash_call_permission_status": {
            "READ_PHONE_STATE": "DENIED",
            "READ_CALL_LOG": "DENIED",
            "ANSWER_PHONE_CALLS": "DENIED"
        },
        "accounts_list": [],
        "gms_incoming_call_retriever_eligibility": "not_eligible",
        "family_device_id": "28d5d418-b9e1-45b1-b144-b0a50445a8ba",
        "fb_ig_device_id": [],
        "device_emails": [],
        "try_num": 1,
        "lois_settings": {"lois_token": ""},
        "event_step": "home_page",
        "headers_infra_flow_id": "6cad1397-9f88-4f39-b73c-d9a1911940f8",
        "openid_tokens": {},
        "contact_point": "mrsxr.test@gmail.com",
        "waterfall_id": "425c3c89-29a5-4015-8589-3a2c3f89776c"
    },
    "server_params": {
        "should_trigger_override_login_2fa_action": 0,
        "is_from_logged_out": 0,
        "should_trigger_override_login_success_action": 0,
        "login_credential_type": "none",
        "server_login_source": "login",
        "waterfall_id": "425c3c89-29a5-4015-8589-3a2c3f89776c",
        "two_step_login_type": "one_step_login",
        "login_source": "Login",
        "is_platform_login": 0,
        "login_entry_point": "logged_out",
        "INTERNAL__latency_qpl_marker_id": 36707139,
        "is_from_aymh": 0,
        "offline_experiment_group": None,
        "is_from_landing_page": 0,
        "left_nav_button_action": "BACK",
        "password_text_input_id": "cyu18f:153",
        "is_from_empty_password": 0,
        "is_from_msplit_fallback": 0,
        "ar_event_source": "login_home_page",
        "username_text_input_id": "cyu18f:152",
        "layered_homepage_experiment_group": None,
        "device_id": "1599219345225378",
        "login_surface": "login_home",
        "INTERNAL__latency_qpl_instance_id": 78410233500631,
        "reg_flow_source": "aymh_single_profile_native_integration_point",
        "is_caa_perf_enabled": 1,
        "credential_type": "password",
        "is_from_password_entry_page": 0,
        "caller": "gslr",
        "family_device_id": "28d5d418-b9e1-45b1-b144-b0a50445a8ba",
        "is_from_assistive_id": 0,
        "access_flow_version": "pre_mt_behavior",
        "is_from_logged_in_switcher": 0
    }
}

DATA = {
    "app_id": "com.bloks.www.bloks.caa.login.async.send_login_request",
    "params": json.dumps(PAYLOAD, separators=(",", ":")),
    "locale": "en_US",
    "client_country_code": "bd",
    "method": "post"
}

if __name__ == "__main__":
    print(f"Sending raw test request to {URL}...")
    response = requests.post(URL, headers=HEADERS, data=DATA, timeout=15)
    print("HTTP Status Code:", response.status_code)
    print("HTTP Response Body:", response.text)
