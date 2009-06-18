/* Copyright © 2009 Jakub Wilk
 *
 * This package is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; version 2 dated June, 1991.
 */

#ifndef PDF2DJVU_I18N
#define PDF2DJVU_I18N

#include "version.hh"
#include "paths.hh"

static inline void N_(const char *message_id)
{
  return;
}

#ifdef ENABLE_NLS

#include <libintl.h>

static inline const char * _(const char *message_id)
{
  return gettext(message_id);
}

namespace i18n
{

  static inline void setup_locale()
  {
    setlocale(LC_ALL, "");
    /* Deliberately ignore errors. */
  }

  static inline void setup()
  {
    setup_locale();
    bindtextdomain(PACKAGE_NAME, paths::localedir);
    /* Deliberately ignore errors. */
    textdomain(PACKAGE_NAME);
    /* Deliberately ignore errors. */
  }
}

#else

static inline const char * ngettext(const char *message_id, const char *message_id_plural, unsigned long int n)
{
  return n == 1 ? message_id : message_id_plural;
}

static inline const char * _(const char *message_id)
{
  return message_id;
}

namespace i18n
{
  static inline void setup_locale()
  {
    setlocale(LC_CTYPE, "");
    /* Deliberately ignore errors. */
  }

  static inline void setup()
  {
    setup_locale();
  }
}

#endif

#endif

// vim:ts=2 sw=2 et