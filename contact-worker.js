/**
 * Genesis AI — Consultation Form → Telegram Notification
 * Cloudflare Worker
 *
 * Environment Variables (set in Cloudflare dashboard → Settings → Variables):
 *   BOT_TOKEN   → your Telegram bot token (never expose in code)
 *   CHAT_ID     → 7937373529
 */

const ALLOWED_ORIGINS = [
  'https://genesis-agenticai.com',
  'https://www.genesis-agenticai.com',
  'https://jacobthebillionaire.github.io',  // GitHub Pages fallback
];

export default {
  async fetch(request, env) {
    // ── CORS pre-flight ──────────────────────────────────────────────────────
    const origin = request.headers.get('Origin') || '';
    const corsHeaders = {
      'Access-Control-Allow-Origin' : ALLOWED_ORIGINS.includes(origin) ? origin : ALLOWED_ORIGINS[0],
      'Access-Control-Allow-Methods': 'POST, OPTIONS',
      'Access-Control-Allow-Headers': 'Content-Type',
    };

    if (request.method === 'OPTIONS') {
      return new Response(null, { status: 204, headers: corsHeaders });
    }

    if (request.method !== 'POST') {
      return new Response('Method Not Allowed', { status: 405, headers: corsHeaders });
    }

    // ── Parse body ───────────────────────────────────────────────────────────
    let data;
    try {
      data = await request.json();
    } catch {
      return new Response('Bad Request', { status: 400, headers: corsHeaders });
    }

    const {
      firstName  = '',
      lastName   = '',
      email      = '',
      phone      = '',
      company    = '',
      revenue    = '',
      employees  = '',
      challenge  = '',
      submittedAt = '',
    } = data;

    const fullName = `${firstName} ${lastName}`.trim();

    // ── Build Telegram message ────────────────────────────────────────────────
    const message = [
      `🔥 *NEW CONSULTATION REQUEST*`,
      ``,
      `👤 *Name:* ${esc(fullName)}`,
      `📧 *Email:* ${esc(email)}`,
      `📞 *Phone:* ${esc(phone)}`,
      `🏢 *Company:* ${esc(company)}`,
      `💰 *Annual Revenue:* ${esc(revenue)}`,
      `👥 *Employees:* ${esc(employees)}`,
      ``,
      `💬 *Challenge:*`,
      esc(challenge || 'Not provided'),
      ``,
      `🕐 *Submitted:* ${esc(submittedAt)} (LA time)`,
    ].join('\n');

    // Inline action buttons
    const replyMarkup = {
      inline_keyboard: [
        [
          { text: '✍️ Write Outreach',  callback_data: `outreach:${company}` },
          { text: '📞 Call Script',      callback_data: `callscript:${company}` },
        ],
        [
          { text: '📋 Add to CRM',       callback_data: `addcrm:${fullName}|${email}|${company}` },
          { text: '⏰ Set Follow-Up',    callback_data: `remind:Follow up with ${fullName} from ${company}` },
        ],
      ],
    };

    // ── Send to Telegram ─────────────────────────────────────────────────────
    const tgRes = await fetch(
      `https://api.telegram.org/bot${env.BOT_TOKEN}/sendMessage`,
      {
        method : 'POST',
        headers: { 'Content-Type': 'application/json' },
        body   : JSON.stringify({
          chat_id     : env.CHAT_ID,
          text        : message,
          parse_mode  : 'Markdown',
          reply_markup: replyMarkup,
        }),
      }
    );

    if (!tgRes.ok) {
      const err = await tgRes.text();
      console.error('Telegram error:', err);
      return new Response('Notification failed', { status: 502, headers: corsHeaders });
    }

    return new Response(JSON.stringify({ ok: true }), {
      status : 200,
      headers: { ...corsHeaders, 'Content-Type': 'application/json' },
    });
  },
};

// Escape Markdown special chars so the message renders cleanly
function esc(str) {
  return String(str).replace(/[_*[\]()~`>#+=|{}.!-]/g, '\\$&');
}
