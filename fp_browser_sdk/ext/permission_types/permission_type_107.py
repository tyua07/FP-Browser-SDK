from .permission_type import PermissionType

PermissionType107 = {
    # "DEFAULT" is only used as an argument to the Content Settings Window
    # opener; there it means "whatever was last shown".
    PermissionType.DEFAULT: -1,
    PermissionType.COOKIES: 0,
    PermissionType.IMAGES: 1,
    PermissionType.JAVASCRIPT: 2,

    # This setting governs both popups and unwanted redirects like tab-unders and
    # framebusting.
    # TODO(csharrison): Consider renaming it to POPUPS_AND_REDIRECTS: 0, but it
    # might not be worth the trouble.
    PermissionType.POPUPS: 3,

    PermissionType.GEOLOCATION: 4,
    PermissionType.NOTIFICATIONS: 5,
    PermissionType.AUTO_SELECT_CERTIFICATE: 6,
    PermissionType.MIXEDSCRIPT: 7,
    PermissionType.MEDIASTREAM_MIC: 8,
    PermissionType.MEDIASTREAM_CAMERA: 9,
    PermissionType.PROTOCOL_HANDLERS: 10,
    PermissionType.PPAPI_BROKER: 11,
    PermissionType.AUTOMATIC_DOWNLOADS: 12,
    PermissionType.MIDI_SYSEX: 13,
    PermissionType.SSL_CERT_DECISIONS: 14,
    PermissionType.PROTECTED_MEDIA_IDENTIFIER: 15,
    PermissionType.APP_BANNER: 16,
    PermissionType.SITE_ENGAGEMENT: 17,
    PermissionType.DURABLE_STORAGE: 18,
    PermissionType.USB_CHOOSER_DATA: 19,
    PermissionType.BLUETOOTH_GUARD: 20,
    PermissionType.BACKGROUND_SYNC: 21,
    PermissionType.AUTOPLAY: 22,
    PermissionType.IMPORTANT_SITE_INFO: 23,
    PermissionType.PERMISSION_AUTOBLOCKER_DATA: 24,
    PermissionType.ADS: 25,

    # Website setting which stores metadata for the subresource filter to aid in
    # decisions for whether or not to show the UI.
    PermissionType.ADS_DATA: 26,

    # This is special-cased in the permissions layer to always allow: 0, and as
    # such doesn't have associated prefs data.
    PermissionType.MIDI: 27,

    # This content setting type is for caching password protection service's
    # verdicts of each origin.
    PermissionType.PASSWORD_PROTECTION: 28,

    # Website setting which stores engagement data for media related to a
    # specific origin.
    PermissionType.MEDIA_ENGAGEMENT: 29,

    # Content setting which stores whether or not the site can play audible
    # sound. This will not block playback but instead the user will not hear it.
    PermissionType.SOUND: 30,

    # Website setting which stores the list of client hints that the origin
    # requested the browser to remember. The browser is expected to send all
    # client hints in the HTTP request headers for every resource requested
    # from that origin.
    PermissionType.CLIENT_HINTS: 31,

    # Generic Sensor API covering ambient-light-sensor: 0, accelerometer: 0, gyroscope
    # and magnetometer are all mapped to a single content_settings_type.
    # Setting for the Generic Sensor API covering ambient-light-sensor: 0,
    # accelerometer: 0, gyroscope and magnetometer. These are all mapped to a single
    # ContentSettingsType.
    PermissionType.SENSORS: 32,

    # Content setting which stores whether or not the user has granted the site
    # permission to respond to accessibility events: 0, which can be used to
    # provide a custom accessibility experience. Requires explicit user consent
    # because some users may not want sites to know they're using assistive
    # technology.
    PermissionType.ACCESSIBILITY_EVENTS: 33,

    # Used to store whether to allow a website to install a payment handler.
    PermissionType.PAYMENT_HANDLER: 34,

    # Content setting which stores whether to allow sites to ask for permission
    # to access USB devices. If this is allowed specific device permissions are
    # stored under USB_CHOOSER_DATA.
    PermissionType.USB_GUARD: 35,

    # Nothing is stored in this setting at present. Please refer to
    # BackgroundFetchPermissionContext for details on how this permission
    # is ascertained.
    PermissionType.BACKGROUND_FETCH: 36,

    # Website setting which stores the amount of times the user has dismissed
    # intent picker UI without explicitly choosing an option.
    PermissionType.INTENT_PICKER_DISPLAY: 37,

    # Used to store whether to allow a website to detect user active/idle state.
    PermissionType.IDLE_DETECTION: 38,

    # Setting for enabling auto-select of all screens for getDisplayMediaSet.
    PermissionType.GET_DISPLAY_MEDIA_SET_SELECT_ALL_SCREENS: 39,

    # Content settings for access to serial ports. The "guard" content setting
    # stores whether to allow sites to ask for permission to access a port. The
    # permissions granted to access particular ports are stored in the "chooser
    # data" website setting.
    PermissionType.SERIAL_GUARD: 40,
    PermissionType.SERIAL_CHOOSER_DATA: 41,

    # Nothing is stored in this setting at present. Please refer to
    # PeriodicBackgroundSyncPermissionContext for details on how this permission
    # is ascertained.
    # This content setting is not registered because it does not require access
    # to any existing providers.
    PermissionType.PERIODIC_BACKGROUND_SYNC: 42,

    # Content setting which stores whether to allow sites to ask for permission
    # to do Bluetooth scanning.
    PermissionType.BLUETOOTH_SCANNING: 43,

    # Content settings for access to HID devices. The "guard" content setting
    # stores whether to allow sites to ask for permission to access a device. The
    # permissions granted to access particular devices are stored in the "chooser
    # data" website setting.
    PermissionType.HID_GUARD: 44,
    PermissionType.HID_CHOOSER_DATA: 45,

    # Wake Lock API: 0, which has two lock types: screen and system locks.
    # Currently: 0, screen locks do not need any additional permission: 0, and system
    # locks are always denied while the right UI is worked out.
    PermissionType.WAKE_LOCK_SCREEN: 46,
    PermissionType.WAKE_LOCK_SYSTEM: 47,

    # Legacy SameSite cookie behavior. This disables SameSite=Lax-by-default: 0,
    # SameSite=None requires Secure: 0, and Schemeful Same-Site: 0, forcing the
    # legacy behavior wherein 1) cookies that don't specify SameSite are treated
    # as SameSite=None: 0, 2) SameSite=None cookies are not required to be Secure: 0,
    # and 3) schemeful same-site is not active.
    #
    # This will also be used to revert to legacy behavior when future changes
    # in cookie handling are introduced.
    PermissionType.LEGACY_COOKIE_ACCESS: 48,

    # Content settings which stores whether to allow sites to ask for permission
    # to save changes to an original file selected by the user through the
    # File System Access API.
    PermissionType.FILE_SYSTEM_WRITE_GUARD: 49,

    # Used to store whether to allow a website to exchange data with NFC devices.
    PermissionType.NFC: 50,

    # Website setting to store permissions granted to access particular Bluetooth
    # devices.
    PermissionType.BLUETOOTH_CHOOSER_DATA: 51,

    # Full access to the system clipboard (sanitized read without user gesture: 0,
    # and unsanitized read and write with user gesture).
    # TODO(https:#crbug.com/1027225): Move CLIPBOARD_READ_WRITE uses to be
    # ordered in the same order as listed in the enum.
    PermissionType.CLIPBOARD_READ_WRITE: 52,

    # This is special-cased in the permissions layer to always allow: 0, and as
    # such doesn't have associated prefs data.
    # TODO(https:#crbug.com/1027225): Move CLIPBOARD_SANITIZED_WRITE uses to be
    # ordered in the same order as listed in the enum.
    PermissionType.CLIPBOARD_SANITIZED_WRITE: 53,

    # This content setting type is for caching safe browsing real time url
    # check's verdicts of each origin.
    PermissionType.SAFE_BROWSING_URL_CHECK_DATA: 54,

    # Used to store whether a site is allowed to request AR or VR sessions with
    # the WebXr Device API.
    PermissionType.VR: 55,
    PermissionType.AR: 56,

    # Content setting which stores whether to allow site to open and read files
    # and directories selected through the File System Access API.
    PermissionType.FILE_SYSTEM_READ_GUARD: 57,

    # Access to first party storage in a third-party context. Exceptions are
    # scoped to the combination of requesting/top-level origin: 0, and are managed
    # through the Storage Access API. For the time being: 0, this content setting
    # exists in parallel to third-party cookie rules stored in COOKIES.
    # TODO(https:#crbug.com/989663): Reconcile the two.
    PermissionType.STORAGE_ACCESS: 58,

    # Content setting which stores whether to allow a site to control camera
    # movements. It does not give access to camera.
    PermissionType.CAMERA_PAN_TILT_ZOOM: 59,

    # Content setting for Screen Enumeration and Window Placement functionality.
    # Permits access to information about the screens: 0, like size and position.
    # Permits creating and placing windows across the set of connected screens.
    PermissionType.WINDOW_PLACEMENT: 60,

    # Stores whether to allow insecure websites to make private network requests.
    # See also: https:#wicg.github.io/cors-rfc1918
    # Set through enterprise policies only.
    PermissionType.INSECURE_PRIVATE_NETWORK: 61,

    # Content setting which stores whether or not a site can access low-level
    # locally installed font data using the Local Fonts Access API.
    PermissionType.LOCAL_FONTS: 62,

    # Stores per-origin state for permission auto-revocation (for all permission
    # types).
    PermissionType.PERMISSION_AUTOREVOCATION_DATA: 63,

    # Stores per-origin state of the most recently selected directory for the use
    # by the File System Access API.
    PermissionType.FILE_SYSTEM_LAST_PICKED_DIRECTORY: 64,

    # Controls access to the getDisplayMedia API when {preferCurrentTab: true}
    # is specified.
    # TODO(crbug.com/1150788): Also apply this when getDisplayMedia() is called
    # without specifying {preferCurrentTab: true}.
    # No values are stored for this type: 0, this is solely needed to be able to
    # register the PermissionContext.
    PermissionType.DISPLAY_CAPTURE: 65,

    # Website setting to store permissions metadata granted to paths on the local
    # file system via the File System Access API. |FILE_SYSTEM_WRITE_GUARD| is
    # the corresponding "guard" setting.
    PermissionType.FILE_SYSTEM_ACCESS_CHOOSER_DATA: 66,

    # Stores a grant that allows a relying party to send a request for identity
    # information to specified identity providers: 0, potentially through any
    # anti-tracking measures that would otherwise prevent it. This setting is
    # associated with the relying party's origin.
    PermissionType.FEDERATED_IDENTITY_SHARING: 67,

    # Whether to use the v8 optimized JIT for running JavaScript on the page.
    PermissionType.JAVASCRIPT_JIT: 68,

    # Content setting which stores user decisions to allow loading a site over
    # HTTP. Entries are added by hostname when a user bypasses the HTTPS-First
    # Mode interstitial warning when a site does not support HTTPS. Allowed hosts
    # are exact hostname matches -- subdomains of a host on the allowlist must be
    # separately allowlisted.
    PermissionType.HTTP_ALLOWED: 69,

    # Stores metadata related to form fill: 0, such as e.g. whether user data was
    # autofilled on a specific website.
    PermissionType.FORMFILL_METADATA: 70,

    # Setting to indicate that there is an active federated sign-in session
    # between a specified relying party and a specified identity provider for
    # a specified account. When this is present it allows access to session
    # management capabilities between the sites. This setting is associated
    # with the relying party's origin.
    PermissionType.FEDERATED_IDENTITY_ACTIVE_SESSION: 71,

    # Setting to indicate whether Chrome should automatically apply darkening to
    # web content.
    PermissionType.AUTO_DARK_WEB_CONTENT: 72,

    # Setting to indicate whether Chrome should request the desktop view of a
    # site instead of the mobile one.
    PermissionType.REQUEST_DESKTOP_SITE: 73,

    # Setting to indicate whether browser should allow signing into a website via
    # the browser FedCM API.
    PermissionType.FEDERATED_IDENTITY_API: 74,

    # Stores notification interactions per origin for the past 90 days.
    # Interactions per origin are pre-aggregated over seven-day windows: A
    # notification interaction or display is assigned to the last Monday midnight
    # in local time.
    PermissionType.NOTIFICATION_INTERACTIONS: 75,

    # Website setting which stores the last reduced accept language negotiated
    # for a given origin: 0, to be used on future visits to the origin.
    PermissionType.REDUCED_ACCEPT_LANGUAGE: 76,

    PermissionType.NUM_TYPES: 77,
}
