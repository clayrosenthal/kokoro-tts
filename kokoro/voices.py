"""Voice definitions for text-to-speech conversion."""

from enum import Enum
from dataclasses import dataclass
from typing import Optional, Union


class KLanguage(Enum):
    """Available languages for text-to-speech conversion."""
    AMERICAN_ENGLISH = "a"
    BRITISH_ENGLISH = "b"
    SPANISH = "e"
    FRENCH = "f"
    HINDI = "h"
    ITALIAN = "i"
    BRAZILIAN_PORTUGUESE = "p"
    JAPANESE = "j"
    MANDARIN_CHINESE = "z"

    @classmethod
    def get_language_by_iso(cls, iso: str) -> "KLanguage":
        """Get a language by its ISO code."""
        return cls(KLANGUAGE_ALIASES.get(iso, iso))

KLANGUAGE_ALIASES = {
    'en-us': 'a',
    'en-gb': 'b',
    'es': 'e',
    'fr-fr': 'f',
    'hi': 'h',
    'it': 'i',
    'pt-br': 'p',
    'ja': 'j',
    'zh': 'z',
}


@dataclass
class KVoiceInfo:
    """Information about a voice."""
    name: str  # Internal name used by the TTS system
    sha256: str  # SHA256 hash of the voice model
    gender: str  # "F" or "M"
    lang_code: KLanguage  # Single-letter language code (a, b, e, f, h, i, p, j, z)
    quality_grade: Optional[str] = None  # Overall quality grade (A-F)
    target_quality: Optional[str] = None  # Target quality grade (A-F)
    training_duration: Optional[str] = None  # Training duration category
    traits: Optional[str] = None  # Emoji traits
    cc_by: Optional[str] = None  # Attribution if under CC BY license


class KVoiceOption(Enum):
    """Available voices for text-to-speech conversion."""
    
    # American English Voices
    AF_HEART = KVoiceInfo("af_heart", "0ab5709b", "F", KLanguage.AMERICAN_ENGLISH, "A", None, None, "❤️")
    AF_ALLOY = KVoiceInfo("af_alloy", "6d877149", "F", KLanguage.AMERICAN_ENGLISH, "C", "B", "MM minutes")
    AF_AOEDE = KVoiceInfo("af_aoede", "c03bd1a4", "F", KLanguage.AMERICAN_ENGLISH, "C+", "B", "H hours")
    AF_BELLA = KVoiceInfo("af_bella", "8cb64e02", "F", KLanguage.AMERICAN_ENGLISH, "A-", "A", "HH hours", "🔥")
    AF_JESSICA = KVoiceInfo("af_jessica", "cdfdccb8", "F", KLanguage.AMERICAN_ENGLISH, "D", "C", "MM minutes")
    AF_KORE = KVoiceInfo("af_kore", "8bfbc512", "F", KLanguage.AMERICAN_ENGLISH, "C+", "B", "H hours")
    AF_NICOLE = KVoiceInfo("af_nicole", "c5561808", "F", KLanguage.AMERICAN_ENGLISH, "B-", "B", "HH hours", "🎧")
    AF_NOVA = KVoiceInfo("af_nova", "e0233676", "F", KLanguage.AMERICAN_ENGLISH, "C", "B", "MM minutes")
    AF_RIVER = KVoiceInfo("af_river", "e149459b", "F", KLanguage.AMERICAN_ENGLISH, "D", "C", "MM minutes")
    AF_SARAH = KVoiceInfo("af_sarah", "49bd364e", "F", KLanguage.AMERICAN_ENGLISH, "C+", "B", "H hours")
    AF_SKY = KVoiceInfo("af_sky", "c799548a", "F", KLanguage.AMERICAN_ENGLISH, "C-", "B", "M minutes")
    AM_ADAM = KVoiceInfo("am_adam", "ced7e284", "M", KLanguage.AMERICAN_ENGLISH, "F+", "D", "H hours")
    AM_ECHO = KVoiceInfo("am_echo", "8bcfdc85", "M", KLanguage.AMERICAN_ENGLISH, "D", "C", "MM minutes")
    AM_ERIC = KVoiceInfo("am_eric", "ada66f0e", "M", KLanguage.AMERICAN_ENGLISH, "D", "C", "MM minutes")
    AM_FENRIR = KVoiceInfo("am_fenrir", "98e507ec", "M", KLanguage.AMERICAN_ENGLISH, "C+", "B", "H hours")
    AM_LIAM = KVoiceInfo("am_liam", "c8255075", "M", KLanguage.AMERICAN_ENGLISH, "D", "C", "MM minutes")
    AM_MICHAEL = KVoiceInfo("am_michael", "9a443b79", "M", KLanguage.AMERICAN_ENGLISH, "C+", "B", "H hours")
    AM_ONYX = KVoiceInfo("am_onyx", "e8452be1", "M", KLanguage.AMERICAN_ENGLISH, "D", "C", "MM minutes")
    AM_PUCK = KVoiceInfo("am_puck", "dd1d8973", "M", KLanguage.AMERICAN_ENGLISH, "C+", "B", "H hours")
    AM_SANTA = KVoiceInfo("am_santa", "7f2f7582", "M", KLanguage.AMERICAN_ENGLISH, "D-", "C", "M minutes")

    # British English Voices
    BF_ALICE = KVoiceInfo("bf_alice", "d292651b", "F", KLanguage.BRITISH_ENGLISH, "D", "C", "MM minutes")
    BF_EMMA = KVoiceInfo("bf_emma", "d0a423de", "F", KLanguage.BRITISH_ENGLISH, "B-", "B", "HH hours")
    BF_ISABELLA = KVoiceInfo("bf_isabella", "cdd4c370", "F", KLanguage.BRITISH_ENGLISH, "C", "B", "MM minutes")
    BF_LILY = KVoiceInfo("bf_lily", "6e09c2e4", "F", KLanguage.BRITISH_ENGLISH, "D", "C", "MM minutes")
    BM_DANIEL = KVoiceInfo("bm_daniel", "fc3fce4e", "M", KLanguage.BRITISH_ENGLISH, "D", "C", "MM minutes")
    BM_FABLE = KVoiceInfo("bm_fable", "d44935f3", "M", KLanguage.BRITISH_ENGLISH, "C", "B", "MM minutes")
    BM_GEORGE = KVoiceInfo("bm_george", "f1bc8122", "M", KLanguage.BRITISH_ENGLISH, "C", "B", "MM minutes")
    BM_LEWIS = KVoiceInfo("bm_lewis", "b5204750", "M", KLanguage.BRITISH_ENGLISH, "D+", "C", "H hours")

    # Japanese Voices
    JF_ALPHA = KVoiceInfo("jf_alpha", "1bf4c9dc", "F", KLanguage.JAPANESE, "C+", "B", "H hours")
    JF_GONGITSUNE = KVoiceInfo("jf_gongitsune", "1b171917", "F", KLanguage.JAPANESE, "C", "B", "MM minutes", None, "gongitsune")
    JF_NEZUMI = KVoiceInfo("jf_nezumi", "d83f007a", "F", KLanguage.JAPANESE, "C-", "B", "M minutes", None, "nezuminoyomeiri")
    JF_TEBUKURO = KVoiceInfo("jf_tebukuro", "0d691790", "F", KLanguage.JAPANESE, "C", "B", "MM minutes", None, "tebukurowokaini")
    JM_KUMO = KVoiceInfo("jm_kumo", "98340afd", "M", KLanguage.JAPANESE, "C-", "B", "M minutes", None, "kumonoito")

    # Mandarin Chinese Voices
    ZF_XIAOBEI = KVoiceInfo("zf_xiaobei", "9b76be63", "F", KLanguage.MANDARIN_CHINESE, "D", "C", "MM minutes")
    ZF_XIAONI = KVoiceInfo("zf_xiaoni", "95b49f16", "F", KLanguage.MANDARIN_CHINESE, "D", "C", "MM minutes")
    ZF_XIAOXIAO = KVoiceInfo("zf_xiaoxiao", "cfaf6f2d", "F", KLanguage.MANDARIN_CHINESE, "D", "C", "MM minutes")
    ZF_XIAOYI = KVoiceInfo("zf_xiaoyi", "b5235dba", "F", KLanguage.MANDARIN_CHINESE, "D", "C", "MM minutes")
    ZM_YUNJIAN = KVoiceInfo("zm_yunjian", "76cbf8ba", "M", KLanguage.MANDARIN_CHINESE, "D", "C", "MM minutes")
    ZM_YUNXI = KVoiceInfo("zm_yunxi", "dbe6e1ce", "M", KLanguage.MANDARIN_CHINESE, "D", "C", "MM minutes")
    ZM_YUNXIA = KVoiceInfo("zm_yunxia", "bb2b03b0", "M", KLanguage.MANDARIN_CHINESE, "D", "C", "MM minutes")
    ZM_YUNYANG = KVoiceInfo("zm_yunyang", "5238ac22", "M", KLanguage.MANDARIN_CHINESE, "D", "C", "MM minutes")

    # Spanish Voices
    EF_DORA = KVoiceInfo("ef_dora", "d9d69b0f", "F", KLanguage.SPANISH, "C", "B", "MM minutes")
    EM_ALEX = KVoiceInfo("em_alex", "5eac53f7", "M", KLanguage.SPANISH, "C", "B", "MM minutes")
    EM_SANTA = KVoiceInfo("em_santa", "aa8620cb", "M", KLanguage.SPANISH, "C", "B", "MM minutes")

    # French Voices
    FF_SIWIS = KVoiceInfo("ff_siwis", "8073bf2d", "F", KLanguage.FRENCH, "B-", "B", "<11 hours", None, "SIWIS")

    # Hindi Voices
    HF_ALPHA = KVoiceInfo("hf_alpha", "06906fe0", "F", KLanguage.HINDI, "C", "B", "MM minutes")
    HF_BETA = KVoiceInfo("hf_beta", "63c0a1a6", "F", KLanguage.HINDI, "C", "B", "MM minutes")
    HM_OMEGA = KVoiceInfo("hm_omega", "b55f02a8", "M", KLanguage.HINDI, "C", "B", "MM minutes")
    HM_PSI = KVoiceInfo("hm_psi", "2f0f055c", "M", KLanguage.HINDI, "C", "B", "MM minutes")

    # Italian Voices
    IF_SARA = KVoiceInfo("if_sara", "6c0b253b", "F", KLanguage.ITALIAN, "C", "B", "MM minutes")
    IM_NICOLA = KVoiceInfo("im_nicola", "234ed066", "M", KLanguage.ITALIAN, "C", "B", "MM minutes")

    # Brazilian Portuguese Voices
    PF_DORA = KVoiceInfo("pf_dora", "07e4ff98", "F", KLanguage.BRAZILIAN_PORTUGUESE, "C", "B", "MM minutes")
    PM_ALEX = KVoiceInfo("pm_alex", "cf0ba8c5", "M", KLanguage.BRAZILIAN_PORTUGUESE, "C", "B", "MM minutes")
    PM_SANTA = KVoiceInfo("pm_santa", "d4210316", "M", KLanguage.BRAZILIAN_PORTUGUESE, "C", "B", "MM minutes")

    

    @property
    def info(self) -> KVoiceInfo:
        """Get the voice information."""
        return self.value

    @property
    def name(self) -> str:
        """Get the voice name."""
        return self.value.name

    @property
    def sha256(self) -> str:
        """Get the voice model SHA256 hash."""
        return self.value.sha256

    @property
    def gender(self) -> str:
        """Get the voice gender (F/M)."""
        return self.value.gender

    @property
    def lang_code(self) -> KLanguage:
        """Get the voice language code."""
        return self.value.lang_code

    @property
    def language(self) -> str:
        """Get the full language name or code."""
        return self.value.lang_code.name

    @property
    def quality_grade(self) -> Optional[str]:
        """Get the voice quality grade."""
        return self.value.quality_grade

    @property
    def is_female(self) -> bool:
        """Check if the voice is female."""
        return self.value.gender == "F"

    @property
    def is_male(self) -> bool:
        """Check if the voice is male."""
        return self.value.gender == "M"

    @classmethod
    def get_by_name(cls, name: str) -> "KVoiceOption":
        """Get a voice by its name.
        
        Args:
            name: The name of the voice to get.
            
        Returns:
            The voice enum value.
            
        Raises:
            ValueError: If no voice with the given name exists.
        """
        for voice in cls:
            if voice.name == name:
                return voice
        raise ValueError(f"No voice named '{name}'")

    @classmethod
    def list_voices(cls, gender: Optional[str] = None, min_grade: Optional[str] = None, lang_code: Optional[Union[str, KLanguage]] = None) -> list["KVoiceOption"]:
        """List available voices with optional filtering.
        
        Args:
            gender: Optional filter by gender ("F" or "M")
            min_grade: Optional minimum quality grade (A-F)
            lang_code: Optional language code (can be alias like 'en-us' or internal code like 'a')
            
        Returns:
            List of voices matching the criteria.
        """
        voices = list(cls)
        
        if gender:
            voices = [v for v in voices if v.gender == gender.upper()]
            
        if min_grade:
            # Convert grade to numeric value (A=4, B=3, etc.)
            def grade_to_num(grade: Optional[str]) -> float:
                if not grade:
                    return -1
                base = 4 - (ord(grade[0]) - ord('A'))
                modifier = grade[1] if len(grade) > 1 else ''
                if modifier == '+':
                    base += 0.3
                elif modifier == '-':
                    base -= 0.3
                return base
            
            min_num = grade_to_num(min_grade)
            voices = [v for v in voices if grade_to_num(v.quality_grade) >= min_num]

        if lang_code:
            # Convert alias to internal code if needed
            internal_code = KLANGUAGE_ALIASES.get(lang_code, lang_code)
            voices = [v for v in voices if v.lang_code == internal_code]
            
        return voices 