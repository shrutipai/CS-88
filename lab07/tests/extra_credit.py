test = {
  'name': 'Extra Credit',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> _, code = lab07_extra_credit()
          >>> hashlib.md5(str.encode(code)).hexdigest()[:6] in ['4fcfe2', '46a074', '5eb654', '0c9e45', 'd948bc', '49cb2f', '66ed1d', '8366e1', 'aa5ddf', '50f1ff', '561c80', '2ced74', 'a7082a', 'acbd81', '2e945a', '2dc360', 'a3f473', 'a55225', '8dc079', 'a49f03', '71bf86', 'e7a90c', '01d6cd', '6ee7f9', '558c8e', '19f24d', 'cfbaea', '8dc7c6', '2393de', '630508', '291e10', '6ab551', '004118', 'b2fafe', 'edc3ea', 'ea8262', '07efa1', '0a4c6a', '923466', 'e848ac', 'a5a30c', '580f8c', '475b55', '66cf78', 'e14d96', 'da9664', '1b8cd5', 'b836ef', 'ae4f2b', '8e1509', '12b4eb', '400d8e', 'e1e801', 'c414d2', '5d0ae0', '334c7e', '64f4ef', '24a3cb', '24d420', '5e8740', '18b3db', '5a5e06', 'ba8cfc', '186ef4', '2fa57c', '280cde', 'c2717b', '1eb450', 'b35ddb', '30e678', '426286', '5a847d', '5a3628', 'd0c445', '4e16f6', '803335', 'afcc44', '224d7f', 'e13a42', 'f62f77', 'f4ca11', '6f51a6', '434439', '60ceb0', '7d9d25', 'a69ca6', '330b46', '575e0c', 'cb7984', '08e37a', 'd6224c', 'bfe1d0', '4b0841', '743938', 'b12dab', 'ef55ad', '4b9315', '4b9faa', '1eaedb', '5a16f6', 'd0beff', '658a6e', '5ef736', 'ca3214', '44adb4', 'b96bfa', '57bb7b', '85c8df', '879c12', 'e19f31', '5e5fec', '542d80', '1c7cf3', 'f9506d', '2b2b8d', '4cfba1', '750179', '44aa2e', 'bddd97', '51a5ab', '3723ca', '1120c8', '27a37e', '3ecd68', '2f7387', 'ebe7f7', '978d28', '2d80af', '2e5927', '990794', '438379', 'c1e243', 'ff6b59', '4382ab', 'aa087c', 'ec9df0', 'a50de4', '159280', 'bfa9bd', '50d614', '228bae', '23c1e5', 'e0a95d', '66f01c', '1d26f1', 'b59c12', '73b550', '21c07a', 'e67a90', '71e5c8', 'c36887', '599bc6', '21c365', '6b7b51', '5d2e39', 'ebb48a', 'cc4395', 'dba594', 'a21bb3', 'b7ad5c', 'c792e9', '65e0e2', '298e55', '04f7f1', 'f71e54', '2aa0d3', '20d5b8', '85dd4b', '7a634a', '63a468', 'bc4d94', 'e415b4', 'e34f7b', '7b3f4f', '4b336b', 'a1eca6', 'a1f3c0', '2a3585', '35b127', '6d4434', '00b139', 'a643e6', 'ec9baf', '696572', 'ebc42b', '5d0244', '2b7416', '40f7cb', '43587e', '97cc30', '3a9648', '0e0039', '26af88', 'd32d88', 'cac180', 'e44d9d', '2914b4', '75600a', '60f412', 'b78896', 'b443ad', '1e9b5b', 'a499ae', '9056fe', 'd57d55', '1276ab', 'aaff7b', '51f0c3', '474326', 'f3ebc9', '5f4571', '91fa37', '708ee9', 'cdb66b', 'e83e10', '1fa880', '763906', 'e89667', '15f1d2', '6c5874', '7301bc', '960826', '8a58ad', '7e19e6', 'c2286c', '7b1b41', 'b90bd4', '289447', 'f13282', '390e7a', '2f2aec', '4c6ad1', '143d43', '6a8391', 'a5a641', '483f41', 'b94b64', '934ddc', '97fc3a', '07dfcd', 'ed766a', '918711', 'f20752', 'd64938', '609e27', '73b60a', '785d50', 'a8f7cb', 'a421ab', '083c18', 'ce20ac', 'dd7cbd', '51dd2e', '1da3c3', '836731', 'f3a78c', 'b7b151', 'af23f9', '585905', '489600', '19754f', '59a718', 'e19cea', '319290', '8e9835', '2ce9e9', '8ebf90', 'fc9df8', '7f63c2', '7bd9db', '2ca837', 'a99f05', 'f6ec1f', '3d5b28', '1c9f58', 'ea53d5', '9c9bc3', 'efba8c', 'e0b6c3', '176ae0', '6c012f', 'c51756', '169029', '1df6a9', '67b56e', 'e9e6f6', 'b6c525', '008416', '33a020', '2fe029', '46e293', 'a4a709', 'e0420a', 'd9058a', '001d76', 'ca038c', 'cffdd6', 'ba52ea', '496ec5', '08c037', 'c5b37c', 'e606ae']
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from lab07 import *
      >>> import hashlib
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
