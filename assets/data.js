// Gegevens die op meerdere pagina's terugkomen. Pas ze alleen hier aan.
window.REELAND = {
  // Vergaderdata, datums als JJJJ-MM-DD. [AANVULLEN] Volgende data en indientermijnen.
  // Voorbeeld: { indienen: '2027-01-11', vergadering: '2027-01-25' },
  // indienen: null betekent dat de indiendatum nog niet is vastgesteld.
  vergaderingen: [
    { indienen: null, vergadering: '2026-10-22' }
  ],
  // Zet op true zodra de stratenlijst volledig is. Tot die tijd zegt de straatzoeker bij een
  // onbekende straat dat de lijst nog wordt aangevuld, in plaats van "hoort er niet bij".
  stratenCompleet: false,
  // [STRATEN] Volledige lijst van het trekkingsgebied, met de buurt erbij.
  straten: [
    { straat: 'Vogelplein', buurt: 'Vogelbuurt' }
  ]
};
